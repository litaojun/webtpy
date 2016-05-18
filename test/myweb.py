#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016��4��27��

@author: li.taojun
'''
import web
import sae
from outh2test import Index
from config import render,urls,runtime
from base import Render as R

cur = {'user':'test'}
class Hello:
    def GET(self):
        web.ctx.session = {}
        tpldata = {"setting":{"webtitle":"testlitaojun"}}
        return render.login(tpldata)
class Login:
    def GET(self):
        tpldata = {"setting":{"webtitle":"testlitaojun"}}
        return render.login(tpldata)
        #return R.render('login')
        
    def POST(self):
        authdata = web.input(username = '', passwd = '')
        print type(authdata)
        print dir(authdata)
        print authdata.user,authdata.passwd
        if authdata:
            if authdata.user == "litaojun" and authdata.passwd == "litaojun":
                cur['user'] = 'litaojun'
                print "---testxxx%s" % cur['user']
                raise web.seeother('/index')
        else:
            raise web.seeother('/')
def authHook(handle):
    path = web.ctx.fullpath.lower()
    print "path=%s" % path
    print "testxxx%s" % cur['user']
    if path == '/':
        pass
    elif path.startswith('/index'):
        if cur['user'] == "tests":
            raise web.seeother('/')
    return handle()
def testweb():
    print "litaojun"
    application = None
    app = web.application(urls, globals())
    if runtime == "SAE":
        application = sae.create_wsgi_app(app.wsgifunc())
    else:
        pass
    return application

app = web.application(urls, globals())

if __name__ == "__main__":
    app.add_processor(authHook)
    app.run()