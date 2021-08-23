
from flask_restful import Resource
from src.controller.store import StoreController
from src.models.store import StoreModel
from src.validations.misc import Miscellaneous
from src.repositories.store import StoreRepository 


class StoreResource(Resource):
    """ StoreResouce class contains methods for getting, deleting and updating single store """
    
    def __init__(self):
        """ Initialise Repository and controller variable neccessary for method action performance """
        self.repository = StoreRepository(model=StoreModel)
        self.controller = StoreController(
            name='Store', repository=self.repository, response=response)
        self.validate_id = Miscellaneous()