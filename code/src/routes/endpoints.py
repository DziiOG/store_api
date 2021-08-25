""" 
endpoints module contains api resources and application routes for accessing those resouces
"""

from src import api
from src.resources.item import ItemResource, ItemListResource
from src.resources.user import UserSignUpResource, UserListResource, UserLoginResource
from src.resources.store import StoreResource, StoreListResource

# ItemResources routes

api.add_resource(ItemResource, '/items/<string:id>')
api.add_resource(ItemListResource, '/items')

#User Resources
api.add_resource(UserSignUpResource, '/signup')
api.add_resource(UserListResource, '/users')
api.add_resource(UserLoginResource, '/login')


api.add_resource(StoreResource, '/stores/<string:id>')
api.add_resource(StoreListResource, '/stores')
