# -*- coding: utf-8 -*-

from argparse import ArgumentParser

from . server import gen_app

parser = ArgumentParser(description='run HTTPPP server')


args = parser.parse_args()

app = gen_app()

app.run(host=app.config['HOST'], port=app.config['PORT'])
