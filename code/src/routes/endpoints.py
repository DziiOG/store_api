from src import api
from src.resources.item import ItemResource

#ItemResources routes

api.add_resource(ItemResource, '/items/<string:id>')


