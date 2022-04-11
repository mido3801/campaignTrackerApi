"""Config objects for flask app"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Application configuration abstract object"""
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevConfig(Config):
    """Config settings to use for development"""
    DEBUG = True
    MONGODB_SETTINGS = {'host': 'mongodb',
                        'db': 'flaskdb',
                        'port': 27017,
                        'username': 'useradmin',
                        'password': 'password'}


env_config = {'development': DevConfig}
