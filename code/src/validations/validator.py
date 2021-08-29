from src.models.user import UserModel
from typing import List
from src.libs import response
from flask import request, g
from functools import wraps
from src import app

class Validator():
    """ Class Validator contains static methods for performing validation operations on methods in resources """
    @staticmethod
    def validate(validator, validation_data="body"):
        """ Validates request params or request body for resource """
        def validation_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                    #validation is params or qquery
                    if validation_data == 'params':
                        #validate with schema template get args as dict
                        validator.load(request.args.to_dict(flat=True))
                        # append validator data to globals for the function to get
                        g.params = request.args.to_dict(flat=True)
                    
                    #comment as above but for body
                    if validation_data == 'body':
                        validator.load(request.get_json())
                        g.body = request.get_json()

                    #return next function
                    return func(*args, **kwargs)
                
            return wrapper
        return validation_decorator

    @staticmethod
    def validate_password():
        """  Validates user  password when signing up  """
        def validate_password_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                   #get user password
                   password = g.body.get('password', None)
                   # get confirm user password
                   confirm_password = g.body.get('confirm_password', None)
                   # compare is the two are the same
                   isCorrect = UserModel.compare_password(password, confirm_password)
                   if isCorrect:
                       #if correct return next function
                       return func(*args, **kwargs)
                   else:
                       #else raise exception
                       raise Exception("confirm password must be equal to password")
                
            #return wrapper
            return wrapper
        #return the decorator validate_password decorator
        return validate_password_decorator
    
    
    @staticmethod
    def exists(keys: List[str]):
        def exists_decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                    for key in keys:
                            if UserModel.objects().filter(**{key:g.body[key]}):
                                raise Exception(f"{key} already exists")
                    return func(*args, **kwargs)
            return wrapper
        return exists_decorator

    
    
serialize = Validator.validate
exists = Validator.exists