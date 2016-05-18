#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016��4��27��

@author: li.taojun
'''
import web
import sae
render = web.template.render('../templates/')
urls = (
    '/','Hello',
    '/index', 'Index'
)

class Index:
    def GET(self):
        return render.index("")

class Hello:
    def GET(self):
        return render.hello()
def testweb():
    app = web.application(urls, globals()).wsgifunc()
    application = sae.create_wsgi_app(app)
    return application

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()