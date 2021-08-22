from flask_restful import Resource
from src.libs import response
from src.models.user import UserModel
from src.controller.user import UserController
from src.repositories.user import UserRepository
from marshmallow import ValidationError
from flask import request
from typing import Dict


class UserResource(Resource):
    def __init__(self):
        self.repository = UserRepository(model=UserModel)
        self.controller = UserController(name="User", repository=self.repository, response=response)



    def post(self):
        pass


