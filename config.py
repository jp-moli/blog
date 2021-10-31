class Config:
    DEBUG = True
    TASTING = True

    #Configuracion de base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/blog"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    SECRET_KEY = "dev"
    DEBUG = True
    TESTING = True
    