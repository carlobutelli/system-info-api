import os


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    FLASK_DEBUG = False
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'this-really-needs-to-be-changed')
    # SECRET_KEY = os.getenv('SECRET_KEY', 'this-really-needs-to-be-changed')


class TestingConfig(BaseConfig):
    """Test environment configuration"""
    DEBUG = True
    DEVELOPMENT = False
    TESTING = True
    FLASK_DEBUG = 1


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEVELOPMENT = True
    TESTING = False


class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


config = {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
        'default': DevelopmentConfig
}
