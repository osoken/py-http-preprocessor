# -*- coding: utf-8 -*-

import os
import json
from logging.config import dictConfig


from flask import Flask, jsonify, request

from . import db


def gen_app(config_object=None, logsetting_file=None):
    if logsetting_file is not None:
        with open(logsetting_file, 'r') as fin:
            dictConfig(json.load(fin))
    elif os.getenv('HTTPPP_LOGGER') is not None:
        with open(os.getenv('HTTPPP_LOGGER'), 'r') as fin:
            dictConfig(json.load(fin))
    app = Flask(__name__)
    app.config.from_object('httppp.config')
    if os.getenv('HTTPPP_CONFIG') is not None:
        app.config.from_envvar('HTTPPP_CONFIG')
    if config_object is not None:
        app.config.update(**config_object)

    @app.route('/api/pp')
    def api_pp():
        return jsonify({})

    return app
