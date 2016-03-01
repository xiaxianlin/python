#-*- coding=utf-8 -*-
import api_controller


def config_route(config):
    # index
    config.add_route('api_comments', '/api/comments')
    config.add_view(api_controller.api_comments, route_name='api_comments')
