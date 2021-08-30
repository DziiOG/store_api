from src.repositories.store import StoreRepository
from src.controller.base import BaseController
from src import app

class StoreController(BaseController):
    def __init__(self):
        self.name = 'Store'
        self.repository = StoreRepository()
        super().__init__(name=self.name, repository=self.repository)
    

    def update_items(self, id, **payload):
        """updates items in the storee model by appending item ids to store.items List field"""
        store = self.repository.update(id, add_to_set__items=payload['items'])
        if store:
            return self.response.successWithData(data=store, message="Store updated successfully"), 200
        return self.response.error(message="No record found", statusCode=404), 404
    


