
from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DB_NAME = os.getenv('DB_NAME')
PORT=os.getenv('PORT')
MONGO_HOST=os.getenv('MONGO_HOST')
DEBUG=os.getenv('FLASK_DEBUG')
