from src.validations.item import ItemBodyValidation, ItemParamsValidation, ItemPatchBodyValidation
from src.security.authenticate import guard, access
from src.controller.item import ItemController
from src.validations import serialize
from src.helpers.misc import ROLES
from flask_restful import Resource
from flask import g, request
from src.helpers.get_request_data import get_data


class ItemResource(Resource):
    """ ItemResouce class contains methods for getting, deleting and updating single item ITem """

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    def get(self, id: str):
        return ItemController().get_by_id(id)

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    @get_data(request)
    @serialize(ItemPatchBodyValidation())
    def patch(self, id: str):
        return ItemController().update(id, **g.body)

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    def delete(self, id: str):
        return ItemController().delete(id)


class ItemListResource(Resource):
    """ ItemListResouce class contains methods for getting and creating Item resouce """

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    @get_data(request)
    @serialize(ItemParamsValidation(), "params")
    def get(self):
        return ItemController().get_docs(**g.params)

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    @get_data(request)
    @serialize(ItemBodyValidation())
    def post(self):
        return ItemController().insert(**g.body)


class ItemStoreResource(Resource):

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    @get_data(request)
    @serialize(validator=ItemParamsValidation(), validation_data="params")
    def get(self, id):
        return ItemController().stores_by_item(id)

