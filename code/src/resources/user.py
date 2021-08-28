from src.validations.user import UserSignUpValidation, UserQueryValidation, UserLoginValidation
from src.validations.validator import serialize, Validator
from src.security.authenticate import guard, access
from src.controller.user import UserController
from src.helpers.misc import ROLES
from flask_restful import Resource
from flask import request, g

class UserLoginResource(Resource):

    @serialize(validator=UserLoginValidation())
    def post(self):
        return UserController().login(**g.body)

class UserSignUpResource(Resource):

    @serialize(validator=UserSignUpValidation())
    @Validator.validate_password()
    @Validator.username_or_email_exists()
    def post(self):
        return UserController().sign_up(**g.body)
           
class UserListResource(Resource):

    @guard()
    @access([ROLES.ADMIN.value])
    @serialize(validator=UserQueryValidation(), validation_data="params")
    def get(self):
            return UserController().get_docs(**g.params)
        
        
        
class UserLogoutResource(Resource):
    @guard()
    def post(self):
        return UserController().logout()
