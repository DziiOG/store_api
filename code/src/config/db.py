from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialise_db(app):
    #app.config['MONGODB_URI'] = "mongodb+srv://DziiOG:JodelOG99@cluster0.0vw6f.mongodb.net/store_db?retryWrites=true&w=majority"
    app.config['MONGODB_SETTINGS'] = {
        'db': 'store_db',
        'host': 'mongodb+srv://DziiOG:JodelOG99@cluster0.0vw6f.mongodb.net/store_db?retryWrites=true&w=majority',
        'port': 9000
    }
    db.init_app(app)
