# -*- coding: utf-8 -*-

import os


DEBUG = True
HOST = '0.0.0.0'
PORT = 8080
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(

    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    ),
    'db.sqlite3'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
