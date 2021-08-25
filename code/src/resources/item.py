from src.validations.item import ItemBodyValidation, ItemParamsValidation, ItemPatchBodyValidation
from src.security.authenticate import Authenticate
from src.validations.validator import Validator
from src.controller.item import ItemController
from flask_restful import Resource
from flask import request, g

class ItemResource(Resource):
    """ ItemResouce class contains methods for getting, deleting and updating single item ITem """

    @Authenticate.is_authenticated_or_authorised()
    def get(self, id: str):
        return ItemController().get_by_id(id)

    @Authenticate.is_authenticated_or_authorised()
    @Validator.validate(ItemPatchBodyValidation())
    def patch(self, id: str):
        return ItemController().update(id, **g.body)

    @Authenticate.is_authenticated_or_authorised()
    def delete(self, id: str):
        return ItemController().delete(id)


class ItemListResource(Resource):
    """ ItemListResouce class contains methods for getting and creating Item resouce """

    @Authenticate.is_authenticated_or_authorised()
    @Validator.validate(ItemParamsValidation(), "params")
    def get(self):
        return ItemController().get_docs(**g.params)

    @Authenticate.is_authenticated_or_authorised()
    @Validator.validate(ItemBodyValidation())
    def post(self):
        return ItemController().insert(**g.body)
