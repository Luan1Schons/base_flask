import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    JWT_SECRET_KEY = "SECRET_KEY"
    # Configurações gerais
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sua-chave-secreta-aqui'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configurações do banco de dados MySQL
    DB_USERNAME = 'root'
    DB_PASSWORD = ''
    DB_HOST = 'localhost'
    DB_PORT = '3306'
    DB_NAME = 'app'

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
