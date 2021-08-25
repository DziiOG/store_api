from src.controller.base import BaseController
from src.repositories.store import StoreRepository

class StoreController(BaseController):
    def __init__(self):
        self.name = 'Store'
        self.repository = StoreRepository()
        super().__init__(name=self.name, repository=self.repository)
