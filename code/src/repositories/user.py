from src.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, model):
        super().__init__(model)
