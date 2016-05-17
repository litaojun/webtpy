#!/usr/bin/python
# -*- coding: utf-8 -*-

import sae
import web

urls = (
    '/','hello'
)

class hello:
    def GET(self):
        return "hello"

app = web.application(urls,globals()).wsgifunc()
application = sae.create_wsgi_app(app)