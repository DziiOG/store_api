from src import api
from src.resources.item import ItemResource, ItemListResource

# ItemResources routes

api.add_resource(ItemResource, '/items/<string:id>')
api.add_resource(ItemListResource, '/items')
