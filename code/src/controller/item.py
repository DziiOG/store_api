from src.repositories.item import ItemRepository
from src.repositories.store import StoreModel
from src.controller.base import BaseController
from src import app

class ItemController(BaseController):
    def __init__(self):
        self.name = 'Item'
        self.repository = ItemRepository()
        self.store_model = StoreModel
        super().__init__(name=self.name, repository=self.repository)


    def stores_by_item(self, id):
        try:
          stores = self.store_model.objects.filter(items__in=[id])
          if stores:
              return self.response.successWithData(data=[store.to_dict() for store in stores], message="Stores fetched successfully")             
          return self.response.successWithData(data=[], statusCode=200), 200       
        except Exception as error:
            app.logger.error(error)
            return self.response.error(message=str(error)), 400
