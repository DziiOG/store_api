from flask_restful import Resource
from src.libs import response
from src.models.user import UserModel
from src.controller.user import UserController
from src.repositories.user import UserRepository
from src.validations.user import UserSignUpValidation, UserQueryValidation, UserLoginValidation
from marshmallow import ValidationError
from src.security.authenticate import Authenticate
from flask import request
from typing import Dict


class UserLoginResource(Resource):
    def __init__(self):
        self.repository = UserRepository(model=UserModel)
        self.controller = UserController(
            name="User", repository=self.repository, response=response)
        self.validate_login = UserLoginValidation()

    def post(self):
        try:
            data = request.get_json()
            self.validate_login.load(data)
            return self.controller.login(**data)

        except Exception as error:
            if isinstance(error, ValidationError):
                return response.error(message=error.messages), 400
            else:
                return response.error(message=str(error)), 400


class UserSignUpResource(Resource):
    def __init__(self):
        self.repository = UserRepository(model=UserModel)
        self.controller = UserController(
            name="User", repository=self.repository, response=response)
        self.validate_sign_up = UserSignUpValidation()

    def post(self):
        try:
            data = request.get_json()
            self.validate_sign_up.load(data)
            confirm_password = data.get('confirm_password')
            password = data.get('password')
            if UserModel.compare_password(password, confirm_password):
                return self.controller.sign_up(**data)
            else:
                raise Exception("confirm password must be equal to password")
        except Exception as error:
            if isinstance(error, ValidationError):
                return response.error(message=error.messages), 400
            else:
                return response.error(message=str(error)), 400


class UserListResource(Resource):
    def __init__(self):
        self.repository = UserRepository(model=UserModel)
        self.controller = UserController(
            name="User", repository=self.repository, response=response)
        self.params_validation = UserQueryValidation()

    @Authenticate.is_authenticated_or_authorised()
    def get(self):
        try:
            params = request.args.to_dict(flat=True)
            self.params_validation.load(params)
            return self.controller.get_docs(**params)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400), 400
