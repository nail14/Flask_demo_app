import os


class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///../db.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = "cerulean"
    OPENAPI_URL_PREFIX = "/api/swagger"
    OPENAPI_SWAGGER_UI_PATH = "/"
    OPENAPI_SWAGGER_UI_VERSION = "3.22.0"


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")