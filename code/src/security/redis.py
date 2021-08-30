from redis.exceptions import AuthenticationError, ConnectionError
from src.libs.response import error
from src import redis_client, app
import json


class CacheUser():
    
    @staticmethod
    def cache_user(authToken: str, user: dict):
            redis_client.set(authToken, json.dumps(user))
        
    
    def remove_cached_user(token):
            redis_client.delete(token)
       
        
        
        
