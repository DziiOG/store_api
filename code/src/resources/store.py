
from src.validations.store import StoreBodyValidation, StoreParamsValidation, StorePatchBodyValidation, StoreItemPatchBodyValidation
from src.security.authenticate import guard, access
from src.controller.store import StoreController
from src.validations.validator import serialize
from src.helpers.misc import ROLES
from flask_restful import Resource
from flask import g

class StoreResource(Resource):
    """ StoreResouce class contains methods for getting, deleting and updating single store """

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    def get(self, id: str):            
        return StoreController().get_by_id(id)
    
    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    @serialize(validator=StorePatchBodyValidation())
    def patch(self, id: str):
            return StoreController().update(id, **g.body)

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    def delete(self, id: str):
        return StoreController().delete(id)
       
class StoreListResource(Resource):
    """ ItemListResouce class contains methods for getting and creating Item resouce """

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    @serialize(validator=StoreParamsValidation(), validation_data="params")
    def get(self):
        return StoreController().get_docs(**g.params)

    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    @serialize(validator=StoreBodyValidation())
    def post(self):
        return StoreController().insert(**g.body)


class StoreItemResource(Resource):
    @guard()
    @access([ROLES.REGULER_USER.value, ROLES.ADMIN.value])
    @serialize(validator=StoreItemPatchBodyValidation())
    def patch(self, id):
        return StoreController().update_items(id, **g.body)
    