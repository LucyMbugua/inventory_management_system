#uri format
#postgresql://user:password@127.0.0.1:5432/databasename
class Config:
    SECRET_KEY ="ADMIN"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class Development(Config):
    """configs for dev env"""
    SECRET_KEY ="ADMIN"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ="postgresql://postgres:ADMIN@127.0.0.1:5432/inventory_db"#Address where postgress db is in your machine
    SQLALCHEMY_ECHO= True
class Staging(Config):
    Debug=False
    SECRET_KEY ="ADMIN"
    SQLALCHEMY_DATABASE_URI ="postgres://fllasgbpmwyciv:b0abccc6caf94677b6db23ecfca7137c89e0b37a69cd1814a55cf547fe3f8803@ec2-46-137-123-136.eu-west-1.compute.amazonaws.com:5432/d7o65v5h6b1jsl"
    SQLALCHEMY_ECHO= True
class Production(Config):
    """configs for production"""
    SECRET_KEY ="administrator"
    SQLALCHEMY_ECHO= False
    