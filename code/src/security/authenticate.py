from src.repositories.user import UserRepository
from src.models.user import UserModel
from src.libs.response import error
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
    def access(roles : List[str] ):
        
        
        """A wrapper to authorize user to access endpoints provided they have certain roles
        """
        def access_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
               try: 
                    #if there is a user making request
                    if g.user:
                        
                        # for every role in the user roles
                        for role in g.user['roles']:
                            
                            #there is a role matches required roles to access resource
                            if role in roles:
                                #set allowed to be true
                                
                                #append user to global g
                                g.user = user
                                
                                return func(*args, **kwargs)
                                
                                
                                #break from loop
                        # if no role matches any
                            
                        # return forbidden 
                        return error("Forbidden", statusCode=403), 403
                        
                        #return the next function
                    
                    # raise this exception
                    raise Exception("Something went wrong processing request")
               except Exception as error:
                   app.logger.error(error)    
                   return error(message=str(error), statusCode=500), 500
                     
            return wrapper
        return access_decorator
        

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
                    
                    # get cached redis user
                    user = json.loads(redis_client.get(token))
                    
                    
                    #decode token
                    isVerified = UserModel.decode_auth_token(token)
                    
                    #store user if verified
                    if isVerified:
                        g.user = user
                        return func(*args, **kwargs)
                    else:
                        return error(message="Unauthorized", statusCode=401), 401


                except KeyError as err:
                    #log error
                    app.logger.error(err)

                    #return error
                    return error(message=str(err), statusCode=400), 400
                
                except Exception as e:
                    
                    app.logger.error(e)

                    return error(message=str(e), statusCode=500), 500
            return wrapper
        return auth_decorator


                   









