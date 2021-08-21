from flask import Flask
from flask_restful import Resource, Api
from src.config.db import initialise_db
from src.config.config import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY
api = Api(app)
initialise_db(app)

from src.routes import endpoints




# CONFIG = config_by_name[os.getenv('ENVIRONMENT')]
# app = Flask(__name__)
# CORS(app, resources={r"/api/*": {"origins": CONFIG.ALLOWED_ORIGINS,
#                                  "methods": ['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH']}})
# # Configure app logger
# @app.before_first_request
# def before_first_request():
#     root = os.path.dirname(os.path.abspath(__file__))
#     log_dir = os.path.join(root, 'logs')
#     log_level = logging.DEBUG if CONFIG.DEBUG else logging.ERROR
#     for handler in app.logger.handlers:
#         app.logger.removeHandler(handler)
#     if not os.path.exists(log_dir):
#         os.mkdir(log_dir)
#     log_file = os.path.join(log_dir, 'app.log')
#     handler = logging.FileHandler(log_file)
#     handler.setFormatter(logging.Formatter("%(asctime)s  {%(pathname)s:%(funcName)s:%(lineno)d} %(levelname)s - %("
#                                            "message)s"))
#     handler.setLevel(log_level)
#     app.logger.addHandler(handler)
#     app.logger.setLevel(log_level)
#     # add handler for sending email for errors
#     if not app.debug:
#         mail_handler = SMTPHandler(
#             mailhost=CONFIG.MAIL_SERVER,
#             fromaddr=CONFIG.MAIL_USERNAME,
#             toaddrs=['peter@completefarmer.com'],
#             subject='Payments API Error'
#         )
#         mail_handler.setLevel(log_level)
#         mail_handler.setFormatter(logging.Formatter('[%(asctimes] %(levelname)s in %(module)s: %(message)s'))
#         app.logger.addHandler(mail_handler)
# app.config['MONGODB_SETTINGS'] = {
#     'host': '{}/{}?retryWrites=true&w=majority'.format(CONFIG.MONGODB_DB_URL, CONFIG.MONGODB_DB)
# }











# from flask_pymongo import PyMongo
# app.config['MONGO_URI'] = "mongodb+srv://DziiOG:JodelOG99@cluster0.0vw6f.mongodb.net/store_db?retryWrites=true&w=majority"
# mongo = PyMongo(app)



