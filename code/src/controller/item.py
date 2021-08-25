from src.controller.base import BaseController
from src.repositories.item import ItemRepository

class ItemController(BaseController):
    def __init__(self):
        self.name = 'Item'
        self.repository = ItemRepository()
        super().__init__(name=self.name, repository=self.repository)
