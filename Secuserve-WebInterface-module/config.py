# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from   decouple import config
from pathlib import Path
class Config(object):
    local = "/Documents/SECUSERVE/SecuServeFiles/"
    

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    DEBUG = True

    # Security
    SESSION_COOKIE_HTTPONLY  = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600
   
    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(Path.home())+str(local)+'db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = True

    # Security
    SESSION_COOKIE_HTTPONLY  = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config( 'DB_ENGINE'   , default='postgresql'    ),
        config( 'DB_USERNAME' , default='1234'       ),
        config( 'DB_PASS'     , default='1234'          ),
        config( 'DB_HOST'     , default='192.168.5.24'     ),
        config( 'DB_PORT'     , default=5432            ),
        config( 'DB_NAME'     , default='secuserve' )
    )

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}
