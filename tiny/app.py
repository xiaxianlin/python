#-*- coding=utf-8 -*-
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from route import config_route

if __name__ == '__main__':
    config = Configurator()
    config_route(config)
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()