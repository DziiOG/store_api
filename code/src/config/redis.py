from redis.exceptions import ConnectionError, AuthenticationError

Client = None
# Connect to Redis (Use password for test and dev environment
def connect_to_redis(redis, CONFIG, app):
    try:
        redis_client = redis.Redis(host=CONFIG.REDIS_HOST, port=CONFIG.REDIS_PORT, db=0)
        if redis_client.ping():
            app.logger.info(f"Connected to Redis on {CONFIG.REDIS_HOST}".format()) 
            Client = redis_client   
    except ConnectionError as err:
        app.logger.error(err)
    except AuthenticationError as err:
        app.logger.error(err)