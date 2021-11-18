from flask import g, request, render_template, make_response
from src.security.authenticate import verify_token
from src.repositories.user import UserRepository
from src.controller.base import BaseController
from src.security.redis import CacheUser
from src.helpers.misc import Status
from functools import wraps
from src import bcrypt
from src import app


class UserController(BaseController):
    """Contains user controller methods for performing operations on users
    """

    def __init__(self):
        self.name = 'User'
        self.repository = UserRepository()
        self.listening = True
        super().__init__(name=self.name, repository=self.repository, listening=self.listening)

        @staticmethod
        @self.on('insert')
        def insert_handler(user):
            data = user.encode_auth_token(
                user_id=user.to_dict().get('_id', None), email=user.to_dict().get('email', None))
            user.user_confirmation_mail(data['auth_token'])

    def pre_insert(self):
        """A wrapper to help registering users
        """
        def pre_insert_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # if status
                if g.body.get('status', None):

                    # delete status
                    del g.body['status']

                # delete confirm password in request body
                del g.body['confirm_password']
                # return next function
                g.body['password'] = bcrypt.generate_password_hash(g.body['password']).decode('utf-8')
                return func(*args, **kwargs)
            return wrapper
        return pre_insert_decorator

    def login(self, **payload):
        """A controller method to login users 
        """
        # get user email
        email = payload.get('email')
        # get user password
        password = payload.get('password')
        # find user with email
        docs = self.repository.get_docs(email=email)

        
        # if there's no user
        if not len(docs):
            # throw this error
            raise Exception("Incorrect Credentials, Please try again")
        else:
            # assign user
            user = docs[0]
            # check if password is correct
            is_correct = user.check_password_correction(password)
            # if correct
            if is_correct:
                # check if user has been activated
                if user.status.value == Status.ACTIVE.value:
                    # generate token
                    data = user.encode_auth_token(
                        user_id=user.to_dict().get('_id', None), email=user.to_dict().get('email', None))
                    # cache user to redis
                    CacheUser.cache_user(data['auth_token'], user.to_dict())
                    # initialise response
                    response_data = dict(
                        **user.to_dict(),
                        auth_token=data['auth_token']
                    )
                    # return response withe data and token
                    return self.response.successWithData(data=response_data, message=f"{self.name} logged in successfully", statusCode=200), 200
                # return is user has not been activated
                return self.response.error(message="User not activated, please check email to activate account and try again", statusCode=400), 400 
            # return this error if password is incorrect
            return self.response.error(message="Incorrect Credentials, Please try again"), 400    

    def activate_user(self):
        params = request.args.to_dict(flat=True)
        payload = verify_token(auth_token=params.get('token', None))
        if payload:
            user_id = payload['sub'].get('user_id', None)
            user = self.repository.get_by_id(user_id)
            if user:
                if user.status.value == Status.IN_ACTIVE.value:
                    user.status = Status.ACTIVE.value
                    user.save()
                    # return redirect("http://localhost:3000/", code=302)  # redirect if we have a separate web app
                    headers = {"Content-Type": "text/html"}
                    return make_response(render_template("confirmation_page.html", email=user.email), 200, headers)
                raise Exception(3)
            raise Exception(2)
        raise Exception(1)
    
    
    def logout(self):
        CacheUser.remove_cached_user(
            request.headers['authorization'].split()[1])
        return self.response.success(message="User logged out successfully")
    
    
