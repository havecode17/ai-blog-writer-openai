##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
