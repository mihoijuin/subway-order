class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "\xc2m\x7f\xb5\x1a\x84\x95\xc7#;)\x0e\x86\'\xd1T`\xdb\xaa\x9bt\xafJ"

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True