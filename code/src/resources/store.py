
from flask_restful import Resource
from marshmallow import ValidationError
from src.controller.store import StoreController
from src.models.store import StoreModel
from src.validations.misc import Miscellaneous
from src.repositories.store import StoreRepository
from src.libs import response
from flask import request

class StoreResource(Resource):
    """ StoreResouce class contains methods for getting, deleting and updating single store """

    def __init__(self):
        """ Initialise Repository and controller variable neccessary for method action performance """
        self.repository = StoreRepository(model=StoreModel)
        self.controller = StoreController(
            name='Store', repository=self.repository, response=response)
        self.validate_id = Miscellaneous()

    def get(self, id: str):
        try:
            # validate get item if id is prensent
            self.validate_id.load({'id': id})
            # return controller method for getting Item by Id
            return self.controller.get_by_id(id)

        except Exception as error:
            # return validation error if validation error occurs
            return response.error(message=error.messages, statusCode=400), 400

    def patch(self, id: str):
        try:
            self.validate_id.load({'id': id})
            data = request.get_json()
            self.patch_body_validation.load(data)
            return self.controller.update(id, **data)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400), 400

    def delete(self, id: str):
        try:
            self.validate_id.load({'id': id})
            return self.controller.delete(id)
        except ValidationError as error:
            return response.error(message=error.messages), 400


class StoreListResource(Resource):
    """ ItemListResouce class contains methods for getting and creating Item resouce """

    def __init__(self):
        """ Initialise Repository and controller variable neccessary for method action performance """
        self.repository = StoreRepository(model=StoreModel)
        self.controller = StoreController(
            name='Store', repository=self.repository, response=response)
        self.validate_id = Miscellaneous()
        self.params_validation = ""

    def get(self):
        try:
            params = request.args.to_dict(flat=True)
            # self.params_validation.load(params)
            return self.controller.get_docs(**params)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400), 400

    def post(self):
        try:
            # request_data = request.get_json()
            self.body_validation.load(request_data)
            return self.controller.insert(**request_data)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400), 400
