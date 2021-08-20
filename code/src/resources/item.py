from flask_restful import Resource
from src.libs import response
from src.models.item import ItemModel
from src.controller.item import ItemController
from src.repositories.item import ItemRepository
from src.validations.item import ItemBodyValidation, ItemParamsValidation, ItemPatchBodyValidation
from src.validations.misc import Miscellaneous
from marshmallow import ValidationError
from flask import request


class ItemResource(Resource):
    def __init__(self):
        self.repository = ItemRepository(model=ItemModel)
        self.controller = ItemController(name='Item', repository=self.repository, response=response)
        self.patch_body_validation = ItemPatchBodyValidation()
        self.validate_id = Miscellaneous()

    def get(self, id):
        try:
            self.validate_id.load({'id': id})
            return self.controller.get_by_id(id)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400)

    def patch(self, id):
        try:
            self.validate_id.load({'id': id})
            data = request.get_json() 
            self.patch_body_validation.load(data)
            return self.controller.update(id, **data)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400)

    def delete(self, id):
        try:
            self.validate_id.load({'id': id})
            return self.controller.delete(id)
        except ValidationError as error:
            return response.error(message=error.messages)


class ItemListResource(Resource):
    def __init__(self):
        self.repository = ItemRepository(model=ItemModel)
        self.controller = ItemController(name='Item', repository=self.repository, response=response)
        self.body_validation = ItemBodyValidation()
        self.params_validation = ItemParamsValidation()

    def get(self):
        try:
            params = request.args.to_dict(flat=True)
            self.params_validation.load(params)
            return self.controller.get_docs(**params)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400), 400
        

    def post(self):
        try: 
            request_data = request.get_json()
            self.body_validation.load(request_data)
            return self.controller.insert(**request_data)
        except ValidationError as error:
            return response.error(message=error.messages, statusCode=400), 400







