from src.validations.item import ItemBodyValidation, ItemParamsValidation, ItemPatchBodyValidation
from src.security.authenticate import Authenticate
from src.validations.validator import Validator
from src.controller.item import ItemController
from flask_restful import Resource
from flask import request, g

class ItemResource(Resource):
    """ ItemResouce class contains methods for getting, deleting and updating single item ITem """

    @Authenticate.auth()
    def get(self, id: str):
        return ItemController().get_by_id(id)

    @Authenticate.auth()
    @Validator.validate(ItemPatchBodyValidation())
    def patch(self, id: str):
        return ItemController().update(id, **g.body)

    @Authenticate.auth()
    def delete(self, id: str):
        return ItemController().delete(id)


class ItemListResource(Resource):
    """ ItemListResouce class contains methods for getting and creating Item resouce """

    @Authenticate.auth()
    @Validator.validate(ItemParamsValidation(), "params")
    def get(self):
        return ItemController().get_docs(**g.params)

    @Authenticate.auth()
    @Validator.validate(ItemBodyValidation())
    def post(self):
        return ItemController().insert(**g.body)


class ItemStoreResource(Resource):

    @Authenticate.auth()
    @Validator.validate(validator=ItemParamsValidation(), validation_data="params")
    def get(self, id):
        return ItemController().stores_by_item(id)

