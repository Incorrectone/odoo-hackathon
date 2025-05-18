import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = b'fc119f23a7bf52997f6037b3b45d346efb8d9144fd73493d91681030addf99be' # Use Secrets
    SECURITY_PASSWORD_SALT = b'hnjchdbndmckiurgebsmkovgituy4g32u9r87ytgfbcndjwkoiduchbcn' # Use Secrets
    JWT_SECRET_KEY = b"uvhsucqwowpehbhcdkcwlwjergbchexjmwskecjdffserdfhgjgcheifdjedwrtyhgtr" # Use Secrets
    REMEMBER_COOKIE_SAMESITE = "strict"
    SESSION_COOKIE_SAMESITE = "strict"
    
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