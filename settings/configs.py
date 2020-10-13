#uri format
#postgresql://user:password@127.0.0.1:5432/databasename
class BaseConfig:
    SECRET_KEY ="ADMIN"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class DevelopmentConfig:
    """configs for dev env"""
    SECRET_KEY ="ADMIN"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ="postgresql://postgres:ADMIN@127.0.0.1:5432/inventory_db"#Address where postgress db is in your machine
    
class ProductionConfig:
    """configs for production"""
    SECRET_KEY ="administrator"
    