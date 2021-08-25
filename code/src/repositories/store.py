from src.repositories.base import BaseRepository
from src.models.store import StoreModel

class StoreRepository(BaseRepository):
    def __init__(self):
        self.model = StoreModel
        super().__init__(model=self.model)
