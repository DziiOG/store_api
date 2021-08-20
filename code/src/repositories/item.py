from src.repositories.base import BaseRepository

class ItemRepository(BaseRepository):
    def __init__(self, model):
        super().__init__(model)


