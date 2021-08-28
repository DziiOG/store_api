from src.repositories.user import UserRepository
from src.controller.base import BaseController
from src.security.redis import CacheUser
from functools import wraps
from flask import g, request
from src import app


class UserController(BaseController):
    def __init__(self):
        self.name = 'User'
        self.repository = UserRepository()
        super().__init__(name=self.name, repository=self.repository)
        
        
        
    def sign_up(self, **payload):
        try:
            # check if user already exists by using username
            email = payload.get('email', None)
            
            data = self.repository.get_docs(email=email)
            
            if data is not None:
                # if user exist raise an exception
                raise Exception("User already exists")
            else:
                if payload.get('status', None):
                    del payload['status']
                    
                del payload['confirm_password']
                # insert new user's data
                result = self.repository.insert(**payload)
                
                # if result return user created details
                return self.response.successWithData(data=result, message=f"{self.name} created succesfully", statusCode=201), 201
        except Exception as error:
            # log the error
            app.logger.error(error)
            # return response with error messsage
            return self.response.error(message=str(error), statusCode=400), 400

    def login(self, **payload):
        try:
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

        except Exception as error:
            app.logger.error(error)
            return self.response.error(message=str(error), statusCode=400), 400

    def logout(self):
        try:
            CacheUser.remove_cached_user(request.headers['authorization'].split()[1])
            return self.response.success(message="User logged out successfully")
        except Exception as error:
            app.logger.error(error)
            return self.response.error(message=str(error), statusCode=400), 400
