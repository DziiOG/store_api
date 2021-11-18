from flask_mongoengine import MongoEngine
db = MongoEngine()


def initialise_db(app, CONFIG) -> None:
    #app.config['MONGODB_URI'] = "mongodb+srv://DziiOG:JodelOG99@cluster0.0vw6f.mongodb.net/store_db?retryWrites=true&w=majority"
    app.config['MONGODB_SETTINGS'] : str = {
        'host': '{}/{}?retryWrites=true&w=majority'.format(CONFIG.MONGODB_DB_URL, CONFIG.MONGODB_DB)
    }
    db.init_app(app)
