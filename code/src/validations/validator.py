from src.validations.misc import Miscellaneous
from marshmallow import ValidationError
from src.models.user import UserModel
from src.libs import response
from flask import request, g
import functools

class Validator():
    @staticmethod
    def validate(validator, validation_data="body"):
        def validation_decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                    if validation_data == 'params':
                        validator.load(request.args.to_dict(flat=True))
                        g.params = request.args.to_dict(flat=True)
                    
                    if validation_data == 'body':
                        validator.load(request.get_json())
                        g.body = request.get_json()
                    return func(*args, **kwargs)
                except ValidationError as error:
                    return response.error(message=error.messages, statusCode=400), 400

            return wrapper
        return validation_decorator

    @staticmethod
    def validate_password():
        def validate_password_decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                try:
                   password = g.body.get('password', None)
                   confirm_password = g.body.get('confirm_password', None)
                   isCorrect = UserModel.compare_password(password, confirm_password)
                   if isCorrect:
                       return func(*args, **kwargs)
                   else:
                       raise Exception("confirm password must be equal to password")
                except Exception as error:
                    return response.error(message=str(error)), 400
            return wrapper
        return validate_password_decorator

    