from src.repositories.store import StoreRepository
from src.controller.base import BaseController

class StoreController(BaseController):
    def __init__(self):
        self.name = 'Store'
        self.repository = StoreRepository()
        super().__init__(name=self.name, repository=self.repository)
