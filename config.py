class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY =



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


Config_options = {
    'development': DevConfig,
    'production': Prodconfig
}