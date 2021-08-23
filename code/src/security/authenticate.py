from functools import wraps
from src import app
from src.models.user import UserModel
from src.libs.response import error
from src.repositories.user import UserRepository
from flask import request, g


#################################################################
# This class is responsible for authentication and authorization
# of users within the API
################################################################

class Authenticate():
    @staticmethod
    def generate_token_auth():
        pass

    @staticmethod
    def is_authenticated_or_authorised():
        """A wrapper to authorize specific roles for specific endpoints :param roles: a list of roles allowed :return:
        """
        def authentication_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    # get request header and split it into two. specificatlly authorisation header Bearer and token
                    token = request.headers['authorization'].split()[1]

                    #decode token
                    user = UserModel.decode_auth_token(token)

                    if user:
                        g.user = user
                    else:
                        return error(message="Unauthorized", statusCode=401), 401

                except KeyError as err:
                    app.logger.error(err)
                    return error(message="Invalid payload", statusCode=400), 400
                
                except Exception as e:
                    app.logger.error(e)
                    return error(message="Sorry, an error occured while processing your request", statusCode=500), 500
            return wrapper
        return authentication_decorator


                   









