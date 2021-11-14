from src.config.config import CONFIG
from src.helpers import errors
from src import app

# Handle generic request exceptions here

if __name__ == '__main__':
    app.logger.info('App running debug: {}'.format(CONFIG.DEBUG))
    app.run(port=CONFIG.PORT, host=CONFIG.HOST)
