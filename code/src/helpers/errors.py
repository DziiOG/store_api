from werkzeug.exceptions import HTTPException
from marshmallow import ValidationError
from src.libs import response
from src import app
import json








@app.errorhandler(ValidationError)
def handle_validation_errors(e):
    app.logger.error(e)
    return response.error(message=e.messages, statusCode=400), 400


@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(e)
    return response.error(message=str(e), statusCode=400), 400
   

@app.errorhandler(HTTPException)
def handle_http_exception(e):
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