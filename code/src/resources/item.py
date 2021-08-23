from flask_restful import Resource
from src.libs import response
from src.models.item import ItemModel
from src.controller.item import ItemController
from src.repositories.item import ItemRepository
from src.validations.item import ItemBodyValidation, ItemParamsValidation, ItemPatchBodyValidation
from src.validations.misc import Miscellaneous
from marshmallow import ValidationError
from src.security.authenticate import Authenticate
from flask import request
from typing import Dict


"""
Item Resouce class

"""
class ItemResource(Resource):
    """ ItemResouce class contains methods for getting, deleting and updating single item ITem """
    
    def __init__(self):
        """ Initialise Repository and controller variable neccessary for method action performance """
        self.repository = ItemRepository(model=ItemModel)
        self.controller = ItemController(
            name='Item', repository=self.repository, response=response)
        self.patch_body_validation = ItemPatchBodyValidation()
        self.validate_id = Miscellaneous()
    
    @Authenticate.is_authenticated_or_authorised()
    def get(self, id: str):
        """ method get Item """
        try:
            #validate get item if id is prensent
            self.validate_id.load({'id': id})


            #return controller method for getting Item by Id
            return self.controller.get_by_id(id)
        except ValidationError as error:
            #return validation error if validation error occurs
            return response.error(message=error.messages, statusCode=400), 400

    @Authenticate.is_authenticated_or_authorised()
    def patch(self, id: str):
        try:
            self.validate_id.load({'id': id})
            data = request.get_json()
            self.patch_body_validation.load(data)
            return self.controller.update(id, **data)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400), 400

    @Authenticate.is_authenticated_or_authorised()
    def delete(self, id: str):
        try:
            self.validate_id.load({'id': id})
            return self.controller.delete(id)
        except ValidationError as error:
            return response.error(message=error.messages), 400


class ItemListResource(Resource):
    """ ItemListResouce class contains methods for getting and creating Item resouce """

    def __init__(self):
        self.repository = ItemRepository(model=ItemModel)
        self.controller = ItemController(
            name='Item', repository=self.repository, response=response)
        self.body_validation = ItemBodyValidation()
        self.params_validation = ItemParamsValidation()

    @Authenticate.is_authenticated_or_authorised()
    def get(self):
        try:
            params = request.args.to_dict(flat=True)
            self.params_validation.load(params)
            return self.controller.get_docs(**params)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400), 400

    @Authenticate.is_authenticated_or_authorised()
    def post(self):
        try:
            request_data = request.get_json()
            self.body_validation.load(request_data)
            return self.controller.insert(**request_data)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400), 400
