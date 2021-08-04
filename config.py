import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "app.db"))

class Config(object):
    SQLALCHEMY_DATABASE_URI = database_file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = 'static'   
    TEMPLATES_FOLDER = 'templates'
    SECRET_KEY = 'kzxvlkghdslkhdg2q36'
    DEBUG = True
    TESTING = True