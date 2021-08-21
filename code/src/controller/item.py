from flask import request
from src.controller.base import BaseController
from src.libs.response import successWithData, error


class ItemController(BaseController):
    def __init__(self, name, repository, response):
        super().__init__(name, repository, response)
