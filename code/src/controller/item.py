from flask import request
from src.controller.base import BaseController
from src.libs.response import successWithData, error


# class Item(Resource,):
#     def __init__(self):

#     def get(self, name):
#         for item in items:
#             if item['name'] == name:
#                 return successWithData(data=item, message="")
#         return error(message="No record found", statusCode=404), 404

#     def post(self, name):
#         data = request.get_json()
#         print(request)
#         item = {'name': name, 'price': data['price']}
#         items.append(item)
#         return successWithData(data=item, message="Item created Successfully", statusCode=201), 201


# class ItemList(Resource):
#     def get(self):
#         return successWithData(data=items, message="Items fetched successfully")



class ItemController(BaseController):
    def __init__(self, name, repository, response):
        super().__init__(name, repository, response)
