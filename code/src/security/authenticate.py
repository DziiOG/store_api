from src.libs.response import error, unauthorized, forbidden
from src.models.user import UserModel
from src import redis_client
from flask import request, g
from functools import wraps
from typing import List
from src import app
import json
import jwt


#################################################################
# This class is responsible for authentication and authorization
# of users within the API
################################################################

verify_token = UserModel.decode_auth_token
generate_token = UserModel.encode_auth_token


class Authenticate():
    @staticmethod
    def generate_token_auth():
        pass

    @staticmethod
    def required_access(roles: List[str]):
        """A wrapper to authorize user to access endpoints provided they have certain roles
        """
        def required_access_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # check roles
                for role in roles:
                    if role == g.user.get('roles', None):
                        return func(*args, **kwargs)
                return forbidden(), 403
            return wrapper
        return required_access_decorator

    @staticmethod
    def auth():
        """A wrapper to authorize user to access endpoints provided if authenticated or they have logged in successfully
        """
        def auth_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # get request header and split it into two. specificatlly authorisation header Bearer and token
                token = request.headers['authorization'].split()[1]
                redis_user = redis_client.get(token)
                if redis_user:
                    # get cached redis user
                    user = json.loads(redis_user)

                    # decode token
                    isVerified = verify_token(token)

                    # store user if verified
                    if isVerified:
                        g.user = user
                        return func(*args, **kwargs)
                    else:
                        return unauthorized(), 401
                return unauthorized(), 401
            return wrapper
        return auth_decorator


guard = Authenticate.auth
access = Authenticate.required_access
