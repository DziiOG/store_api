from werkzeug.exceptions import HTTPException
from src.config.config import CONFIG
from flask import json
from src import app

# Handle generic request exceptions here


@app.errorhandler(HTTPException)
def handle_exception(e):
    """
    Return JSON instead of HTML for HTTP errors.
    """
    # log the error
    app.logger.error(e)
    # Start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response


if __name__ == '__main__':
    app.logger.info('App running debug: {}'.format(CONFIG.DEBUG))
    app.run(port=CONFIG.PORT, host=CONFIG.HOST)
