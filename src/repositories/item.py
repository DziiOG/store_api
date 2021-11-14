from src.repositories.base import BaseRepository
from src.models.item import ItemModel


class ItemRepository(BaseRepository):
    def __init__(self):
        self.model = ItemModel
        super().__init__(model=self.model)
