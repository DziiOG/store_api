
from dotenv import load_dotenv
import os
load_dotenv()

class BaseConfiguration(object):
    """
    Base configuration class to hold common configuration to this application
    """
    DEBUG = False
    TESTING = False
    # Application secret key
    SECRET_KEY = os.getenv('SECRET_KEY')
    # DB Settings
    MONGODB_DB_URL = os.getenv('DB_URI')
    MONGODB_DB = os.getenv('DEV_DB')
    # Default App Settings
    HOST = os.getenv('DEV_HOST')
    PORT = os.getenv('DEV_PORT')

    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS")

    # SMTP Configuration
    MAIL_SERVER = os.getenv('DEV_MAIL_SERVER')
    MAIL_PORT = os.getenv('DEV_MAIL_PORT')
    MAIL_USERNAME = os.getenv('DEV_MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('DEV_MAIL_PASSWORD')


class TestConfig(BaseConfiguration):
    """
    Test configuration inherits from base configuration and override some attributess
    Environmental variables must be set on testing environment (OS). Variables
    are not contained in .env for security reasons
    """
    TESTING = True
    DEBUG = True
    # DB Settings
    MONGODB_DB = os.getenv('TEST_DB')
    HOST = os.getenv('TEST_HOST')
    PORT = os.getenv('TEST_PORT')


class DevConfig(BaseConfiguration):
    """
    Development configuration uses default configuration
    from base configuration for DB and Server
    """
    DEBUG = True
    TESTING = False


class ProdConfig(BaseConfiguration):
    """Environmental variables for production environment must be set on the OS
    Variables are not contained in .env for security reasons
    """


get_config = dict(
    DEV=DevConfig,
    TEST=TestConfig,
    PROD=ProdConfig
)

CONFIG = get_config[os.getenv('ENVIRONMENT')]
