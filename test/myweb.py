#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016��4��27��

@author: li.taojun
'''
import web

render = web.template.render('../templates/')
urls = (
    '/index', 'index'
)

class index:
    def GET(self):
        return render.index("")
def testweb(self):
    app = web.application(urls, globals())
    return app

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()