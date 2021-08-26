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
        try:
            store = self.repository.update(id, add_to_set__items=payload['items'])
            if store:
                return self.response.successWithData(data=store, message="Store updated successfully"), 200
            return self.response.error(message="No record found", statusCode=404), 404
        except Exception as error:
            app.logger.error(error)
            return self.response.error(message=str(error), statusCode=400), 400



