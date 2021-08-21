from flask_mongoengine import MongoEngine
from src.config.config import DB_NAME, PORT, MONGO_HOST
db = MongoEngine()


def initialise_db(app):
    #app.config['MONGODB_URI'] = "mongodb+srv://DziiOG:JodelOG99@cluster0.0vw6f.mongodb.net/store_db?retryWrites=true&w=majority"
    app.config['MONGODB_SETTINGS'] = {
        'db': DB_NAME,
        'host': MONGO_HOST,
        'port': int(PORT)
    }
    db.init_app(app)
