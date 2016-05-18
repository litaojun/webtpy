#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016��5��18��

@author: li.taojun
'''
from config import render,urls
class Index:
    def GET(self):
        return render.index("")