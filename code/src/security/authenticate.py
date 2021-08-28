from src.repositories.user import UserRepository
from werkzeug.security import safe_str_cmp
from src.models.user import UserModel
from src.libs.response import error, unauthorized
from src.libs import response
from src import redis_client
from flask import request, g
from functools import wraps
from typing import List
from src import app
import json


#################################################################
# This class is responsible for authentication and authorization
# of users within the API
################################################################

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
                try:
                    # if there is a user making request
                    for role in roles:
                        if role == g.user.get('roles', None):
                            return func(*args, **kwargs)
                    return response.forbidden(), 403
                except Exception as error:
                    app.logger.error(error)
                    return error(message=str(error), statusCode=500), 500

            return wrapper
        return required_access_decorator

    @staticmethod
    def auth():
        """A wrapper to authorize user to access endpoints provided if authenticated or they have logged in successfully
        """
        def auth_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    # get request header and split it into two. specificatlly authorisation header Bearer and token
                    token = request.headers['authorization'].split()[1]
                    redis_user = redis_client.get(token)
                    if redis_user:
                    # get cached redis user
                        user = json.loads(redis_user)

                        # decode token
                        isVerified = UserModel.decode_auth_token(token)

                        # store user if verified
                        if isVerified:
                            g.user = user
                            return func(*args, **kwargs)
                        else:
                            return unauthorized(), 401
                    return unauthorized(), 401

                except KeyError as err:
                    # log error
                    app.logger.error(err)

                    # return error
                    return error(message=str(err), statusCode=400), 400

                except Exception as e:

                    app.logger.error(e)

                    return error(message=str(e), statusCode=500), 500
            return wrapper
        return auth_decorator


guard = Authenticate.auth
access = Authenticate.required_access
