from src.config.redis import connect_to_redis
from flask_restful import Resource, Api
from src.config.db import initialise_db
from src.config.config import CONFIG
from flask import Flask, Blueprint
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt import JWT
import logging
import redis
import os

#flask application initialization
app = Flask(__name__)


#cors cross orgin resource sharing specification of accessible methods and origins
CORS(app, resources={r"/api/*": {"origins": CONFIG.ALLOWED_ORIGINS,
                                 "methods": ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH']}})



# Configure app logger
@app.before_first_request
def before_first_request():
    root = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(root, 'logs')
    log_level = logging.DEBUG if CONFIG.DEBUG else logging.ERROR
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)
    log_file = os.path.join(log_dir, 'app.log')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter("%(asctime)s  {%(pathname)s:%(funcName)s:%(lineno)d} %(levelname)s - %("
                                           "message)s"))
    handler.setLevel(log_level)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)
    # add handler for sending email for errors
    if not app.debug:
        mail_handler = SMTPHandler(
            mailhost=CONFIG.MAIL_SERVER,
            fromaddr=CONFIG.MAIL_USERNAME,
            toaddrs=['lildzii.wd@gmail.com'],
            subject='Store API Error'
        )
        mail_handler.setLevel(log_level)
        mail_handler.setFormatter(logging.Formatter('[%(asctimes] %(levelname)s in %(module)s: %(message)s'))
        app.logger.addHandler(mail_handler)


#get config
app.config.from_object(CONFIG)

#application blueprint
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

#register blue print
app.register_blueprint(blueprint)


# set application secret key
app.secret_key = CONFIG.SECRET_KEY

#instantiate bcrpyt with flask application
bcrypt = Bcrypt(app)

#instantiate api with flask application
api = Api(app=app, prefix="/api/v1")

#initialise db
initialise_db(app=app, CONFIG=CONFIG)


connect_to_redis(redis=redis, CONFIG=CONFIG, app=app)

#return resources
from src.routes import endpoints




















