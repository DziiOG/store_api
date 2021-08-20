from flask_restful import Resource
from src.libs import response
from src.models.item import ItemModel
from src.controller.item import ItemController
from src.repositories.item import ItemRepository
from flask import request


class ItemResource(Resource):
    def __init__(self):
        self.repository = ItemRepository(model=ItemModel)
        self.controller = ItemController(name='Item', repository=self.repository, response=response)

    def get(self, id):
        return self.controller.get_by_id(id)

    def patch(self, id):
        data = request.get_json()

        print(data)
    
        return self.controller.update(id, payload)




