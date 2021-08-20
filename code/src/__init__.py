from flask import Flask
from flask_restful import Resource, Api
from src.config.db import initialise_db


app = Flask(__name__)
app.secret_key = 'c904d70087ac7d9b078bc7958f89d9fc'
api = Api(app)
initialise_db(app)

from src.routes import endpoints










# from flask_pymongo import PyMongo
# app.config['MONGO_URI'] = "mongodb+srv://DziiOG:JodelOG99@cluster0.0vw6f.mongodb.net/store_db?retryWrites=true&w=majority"
# mongo = PyMongo(app)



