#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016��4��27��

@author: li.taojun
'''
import web
import sae
from outh2test import Index
from config import render,urls
#render = web.template.render('templates')


class Hello:
    def GET(self):
        return render.hello()
def testweb():
    print "litaojun"
    app = web.application(urls, globals()).wsgifunc()
    application = sae.create_wsgi_app(app)
    return application

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()