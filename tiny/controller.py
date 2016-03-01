#-*- coding=utf-8 -*-
from pyramid.response import Response


def comments(request):
    tpl = 'this is index page'
    return Response(tpl)