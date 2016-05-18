#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016��5��18��

@author: li.taojun
'''
import web
import sae
render = web.template.render('templates')
#render = web.template.render('../templates')
urls = (
    '/','Hello',
    '/index', 'Index'
)
        