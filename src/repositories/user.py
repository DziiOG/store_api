from src.repositories.base import BaseRepository
from src.models.user import UserModel


class UserRepository(BaseRepository):
    def __init__(self):
        self.model = UserModel
        super().__init__(model=self.model)
