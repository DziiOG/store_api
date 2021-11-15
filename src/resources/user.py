from src.validations.user import UserSignUpValidation, UserQueryValidation, UserLoginValidation
from src.validations import serialize, validate_password, exists
from src.security.authenticate import guard, access
from src.controller.user import UserController
from src.libs.uploader import upload
from src.helpers.misc import ROLES
from flask_restful import Resource
from flask import g, request

class UserLoginResource(Resource):

    @serialize(validator=UserLoginValidation())
    def post(self):
        return UserController().login(**g.body)

class UserSignUpResource(Resource):
    @upload(request, 'avatar')
    @serialize(validator=UserSignUpValidation())
    @exists(['username', 'email'])
    @validate_password()
    @UserController().pre_insert()
    def post(self):
        return UserController().insert(**g.body)
           
class UserListResource(Resource):

    @guard()
    @access([ROLES.ADMIN.value])
    @serialize(validator=UserQueryValidation(), validation_data="params")
    def get(self):
            return UserController().get_docs(**g.params)
        
class UserActivationResource(Resource):
    
    def get(self):
        return UserController().activate_user()
        
class UserLogoutResource(Resource):
    @guard()
    def post(self):
        return UserController().logout()
