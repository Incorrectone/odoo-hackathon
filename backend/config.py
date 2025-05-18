import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = b'fc119f23a7bf52997f6037b3b45d346efb8d9144fd73493d91681030addf99be'
    SECURITY_PASSWORD_SALT = b'hnjchdbndmckiurgebsmkovgituy4g32u9r87ytgfbcndjwkoiduchbcn'
    JWT_SECRET_KEY = b"this is such a sad day you guys do not understand that I have no idea what I am saying"
    REMEMBER_COOKIE_SAMESITE = "strict"
    SESSION_COOKIE_SAMESITE = "strict"
    
    CELERY_BROKER_URL = 'redis://localhost:6379/0'  
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  
    
    UPLOAD_FOLDER = basedir + '/app/static/uploads'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}