#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016��5��18��

@author: li.taojun
'''
import web
import sae
runtime = 'SAE'
hostip = "localhost"
port = 8080
if runtime == 'SAE':
   render = web.template.render('templates')
else:
   render = web.template.render('../templates')
urls = (
    '/','Login',
    '/index', 'Index',
    '/login','Login',
    '/resource','OtherResouce',
    '/litaojun','DealCode'
)
        