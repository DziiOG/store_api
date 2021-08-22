from src.controller.base import BaseController


class ItemController(BaseController):
    def __init__(self, name, repository, response):
        super().__init__(name, repository, response)
