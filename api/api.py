#!/usr/bin/env python
# -*- coding: utf8 -*-
__author__ = 'varoqua'

from bottle import route, run, abort
import time
from lib.pinterest import Pinterest
import lib.apihelper

def function_test(username,password):
    p = Pinterest()
    p.login(username,password)
    return p

list = {"key":function_test("username","password")}


def get_session(username,password):
    p = list[username]
    return p


@route('/api/pinterest',method='POST')
def post():
    import traceback
    try:
        get = lib.apihelper
        p = get_session(get.user_name(),get.password())
        boards = p.getBoards()
        print boards
        res = p.createPin(board=boards[get.board()],title=get.title(),
                    media='createdynamicmediahere (this should be a link to an image)',
                    posturl='createdynamicposturlhere (this should be a link)'
                )

        print 'pin created: %s' % res
    except:
        return abort(500, traceback.format_exc())


@route('/api/status')
def api_status():
    return {'status':'online', 'servertime':time.time()}


run(host='localhost', port=8080, debug=True)
