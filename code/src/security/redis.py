from src import redis_client, app
from src.libs.response import error
from flask import jsonify
import json
from redis.exceptions import AuthenticationError, ConnectionError


class CacheUser():
    
    @staticmethod
    def cache_user(authToken: str, user: dict):
        try:
            redis_client.set(authToken, json.dumps(user))
        except ConnectionError as err:
            app.logger.error(err)
        except AuthenticationError as err:
            app.logger.error(err)
        except Exception as err:
            app.logger.error(err)
            return error(message=str(error), statusCode=400), 400
            
    
    def remove_cached_user(token):
        try:
            redis_client.delete(token)
        except ConnectionError as err:
            app.logger.error(err)
        except AuthenticationError as err:
            app.logger.error(err)
        except Exception as err:
            app.logger.error(err)
            return error(message=str(error), statusCode=400), 400
            
        
        
        
