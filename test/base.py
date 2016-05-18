#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GarfieltBlog(webpy) is a light weight blog system base on web.py.It is similar 
to WordPress that provides commonly functions and featurs of a blog system.

Homepage and details: http://www.iscsky.net/

Copyright (c) 2012, Garfielt <liuwt123@gmail.com>.
License: MIT (see LICENSE.txt for details)
"""

import web





class _Render:
    def __init__(self):
        self.tplfunc = {}
        self.tpldata = {}
        self.tpldir = ''
        self.tpldata['version'] = 'Setting.version'
        self.tplfunc['UIModule'] = self.UIModule
    


    
    def render(self, tplname, **kwargs):
        self.tpldata['setting'] = ''
        for key in kwargs:
            self.tpldata[key] = kwargs[key]
        return getattr(self.robject(), tplname)(self.tpldata)
    
    def UIModule(self, tplname):
        return self.render(tplname)
        
    def addtplfunc(self, func, quotfunc):
        self.tplfunc[func] = quotfunc
    
   
    
    def result(self, flag, url, msg):
        return self.render('result', flag=flag, url=url, msg=msg)
    
    def robject(self):
        return web.template.render('template/' + self.gettpldir(), globals=self.tplfunc)

Render = _Render()

__ALL__ = ['Render']