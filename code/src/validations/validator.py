from src.validations.misc import Miscellaneous
from marshmallow import ValidationError
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

    