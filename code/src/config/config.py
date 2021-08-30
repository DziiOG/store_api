
from dotenv import load_dotenv
import os

# load all variable from .env file
load_dotenv()



class BaseConfiguration(object):
    """
    Base configuration class to hold common configuration to this application
    """
    DEBUG = False
    TESTING = False
    # Application secret key
    SECRET_KEY : str = os.getenv('SECRET_KEY')
    # DB Settings
    MONGODB_DB_URL : str = os.getenv('DB_URI')
    MONGODB_DB = os.getenv('DEV_DB')
    # Default App Settings
    HOST = os.getenv('DEV_HOST')
    PORT = os.getenv('DEV_PORT')
    
    ALLOWED_ORIGINS : str = os.getenv("ALLOWED_ORIGINS")

    # SMTP Configuration
    MAIL_SERVER = os.getenv('DEV_MAIL_SERVER')
    MAIL_PORT = os.getenv('DEV_MAIL_PORT')
    MAIL_USERNAME = os.getenv('DEV_MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('DEV_MAIL_PASSWORD')
    MAILGUN_EMAIL = os.getenv('MAILGUN_EMAIL')
    MAILGUN_API_BASE_URL = os.getenv('MAILGUN_API_BASE_URL')
    MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')


class TestConfig(BaseConfiguration):
    """
    Test configuration inherits from base configuration and override some attributess
    Environmental variables must be set on testing environment (OS). Variables
    are not contained in .env for security reasons
    """
    TESTING = True
    DEBUG = True
    # DB Settings
    MONGODB_DB : str = os.getenv('TEST_DB')
    HOST  = os.getenv('TEST_HOST')
    PORT = os.getenv('TEST_PORT')
    


class DevConfig(BaseConfiguration):
    """
    Development configuration uses default configuration
    from base configuration for DB and Server
    """
    DEBUG : bool = True
    TESTING : bool = False
    REDIS_PASS = os.getenv('DEV_REDIS_PASS')
    REDIS_HOST = os.getenv('DEV_REDIS_HOST')
    REDIS_PORT = os.getenv('DEV_REDIS_PORT')


class ProdConfig(BaseConfiguration):
    """Environmental variables for production environment must be set on the OS
    Variables are not contained in .env for security reasons
    """


get_config : dict = dict(
    DEV=DevConfig,
    TEST=TestConfig,
    PROD=ProdConfig
)

CONFIG = get_config[os.getenv('ENVIRONMENT')]
