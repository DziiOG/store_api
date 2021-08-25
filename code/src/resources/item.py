from src.validations.item import ItemBodyValidation, ItemParamsValidation, ItemPatchBodyValidation
from src.security.authenticate import Authenticate
from src.validations.validator import Validator
from src.controller.item import ItemController
from flask_restful import Resource
from flask import request, g


"""
Item Resouce class

"""

class ItemResource(Resource):
    """ ItemResouce class contains methods for getting, deleting and updating single item ITem """

    def __init__(self):
        """ Initialise Repository and controller variable neccessary for method action performance """
        self.controller = ItemController()

    @Authenticate.is_authenticated_or_authorised()
    def get(self, id: str):
        return self.controller.get_by_id(id)

    @Authenticate.is_authenticated_or_authorised()
    @Validator.validate(validator=ItemPatchBodyValidation())
    def patch(self, id: str):
            return self.controller.update(id, **data)

    @Authenticate.is_authenticated_or_authorised()
    def delete(self, id: str):
            return self.controller.delete(id)


class ItemListResource(Resource):
    """ ItemListResouce class contains methods for getting and creating Item resouce """
    def __init__(self):
        self.controller = ItemController()
            
    @Authenticate.is_authenticated_or_authorised()
    @Validator.validate(ItemParamsValidation(), validation_data="params")
    def get(self):
            return self.controller.get_docs(**g.params)

    @Authenticate.is_authenticated_or_authorised()
    @Validator.validate(ItemBodyValidation())
    def post(self):
            return self.controller.insert(**g.body)
