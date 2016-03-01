#-*- coding=utf-8 -*-
from pyramid.response import Response
import json


def api_comments(request):
    data = [{'id': 1, 'author': 'Pete Hunt', 'text': 'This is one comment'}, {'id': 2, 'author': 'Jordan Walke', 'text': 'This is *another* comment'}]
    result = json.dumps(data)
    resp = Response(result)
    resp.headerlist.append(('Access-Control-Allow-Origin', '*'))  #Add the access control
    return resp