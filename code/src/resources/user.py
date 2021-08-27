from src.validations.user import UserSignUpValidation, UserQueryValidation, UserLoginValidation
from src.security.authenticate import Authenticate
from src.validations.validator import Validator
from src.controller.user import UserController
from flask_restful import Resource
from flask import request, g

class UserLoginResource(Resource):

    @Validator.validate(validator=UserLoginValidation())
    def post(self):
        return UserController().login(**g.body)

class UserSignUpResource(Resource):

    @Validator.validate(validator=UserSignUpValidation())
    @Validator.validate_password()
    def post(self):
        return UserController().sign_up(**g.body)
           
class UserListResource(Resource):

    @Authenticate.auth()
    @Validator.validate(validator=UserQueryValidation(), validation_data="params")
    def get(self):
            return UserController().get_docs(**g.params)
