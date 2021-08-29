from src.repositories.user import UserRepository
from src.controller.base import BaseController
from src.security.redis import CacheUser
from flask import g, request
from functools import wraps
from src import app


class UserController(BaseController):
    def __init__(self):
        self.name = 'User'
        self.repository = UserRepository()
        super().__init__(name=self.name, repository=self.repository)
        
    @staticmethod
    def pre_insert():
        def pre_insert_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                #if status
                if g.body.get('status', None):
                    
                    #delete status
                    del g.body['status']
                    
                # delete confirm password in request body
                del g.body['confirm_password']
                
                #return next function
                return func(*args, **kwargs)
            return wrapper
        return pre_insert_decorator
          
    def login(self, **payload):
            email = payload.get('email')
            password = payload.get('password')
            user = self.repository.get_docs(raw=True, email=email)
            if user is None:
                raise Exception("Incorrect Credentials, Please try again")
            else:
                is_correct = user[0].check_password_correction(password)
                if is_correct:
                    data = user[0].encode_auth_token(
                        user_id=user[0].to_dict().get('_id', None), email=user[0].to_dict().get('email', None))
                    CacheUser.cache_user(data['auth_token'], user[0].to_dict()) 
                    response_data = dict(
                        **user[0].to_dict(),
                        auth_token=data['auth_token'].decode('utf-8')
                    )
                    return self.response.successWithData(data=response_data, message=f"{self.name} logged in successfully", statusCode=200), 200
                return self.response.error(message="Incorrect Credentials, Please try again"), 400

    def logout(self):
            CacheUser.remove_cached_user(request.headers['authorization'].split()[1])
            return self.response.success(message="User logged out successfully")
       
