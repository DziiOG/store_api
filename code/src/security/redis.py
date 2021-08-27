from src.config.redis import Client
from flask import jsonify
from redis.exceptions import AuthenticationError, ConnectionError


class CacheUser():
    
    @staticmethod
    def cache_user(authToken: str, user: dict):
        try:
            Client.set(str(authToken), jsonify(user))
        except ConnectionError as err:
            app.logger.error(err)
        except AuthenticationError as err:
            app.logger.error(err)
            
    
    def remove_cached_user(token):
        try:
            Client.delete(str(authToken))
        except ConnectionError as err:
            app.logger.error(err)
        except AuthenticationError as err:
            app.logger.error(err)
        
        
        
