""" 
endpoints module contains api resources and application routes for accessing those resouces
"""

from src.resources.user import UserSignUpResource, UserListResource, UserLoginResource
from src.resources.store import StoreResource, StoreListResource, StoreItemResource
from src.resources.item import ItemResource, ItemListResource, ItemStoreResource
from src import api

# ItemResources routes

api.add_resource(ItemResource, '/items/<string:id>')
api.add_resource(ItemStoreResource, '/items/<string:id>/store')
api.add_resource(ItemListResource, '/items')


#User Resources
api.add_resource(UserSignUpResource, '/users/signup')
api.add_resource(UserListResource, '/users')
api.add_resource(UserLoginResource, '/users/login')


api.add_resource(StoreResource, '/stores/<string:id>')
api.add_resource(StoreItemResource, '/stores/<string:id>/item')
api.add_resource(StoreListResource, '/stores')

