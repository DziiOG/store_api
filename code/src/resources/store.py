
from src.validations.store import StoreBodyValidation, StoreParamsValidation, StorePatchBodyValidation, StoreItemPatchBodyValidation
from src.security.authenticate import Authenticate
from src.repositories.store import StoreRepository
from src.controller.store import StoreController
from src.validations.validator import Validator
from src.validations.misc import Miscellaneous
from marshmallow import ValidationError
from src.models.store import StoreModel
from flask_restful import Resource
from src.libs import response
from flask import request, g

class StoreResource(Resource):
    """ StoreResouce class contains methods for getting, deleting and updating single store """

    @Authenticate.auth()
    def get(self, id: str):            
        return StoreController().get_by_id(id)
    
    @Authenticate.auth()
    @Validator.validate(validator=StorePatchBodyValidation())
    def patch(self, id: str):
            return StoreController().update(id, **g.body)

    @Authenticate.auth()
    def delete(self, id: str):
        return StoreController().delete(id)
       
class StoreListResource(Resource):
    """ ItemListResouce class contains methods for getting and creating Item resouce """

    @Authenticate.auth()
    @Validator.validate(validator=StoreParamsValidation(), validation_data="params")
    def get(self):
        return StoreController().get_docs(**g.params)

    @Authenticate.auth()
    @Validator.validate(validator=StoreBodyValidation())
    def post(self):
        return StoreController().insert(**g.body)


class StoreItemResource(Resource):
    @Authenticate.auth()
    @Validator.validate(validator=StoreItemPatchBodyValidation())
    def patch(self, id):
        return StoreController().update_items(id, **g.body)
    