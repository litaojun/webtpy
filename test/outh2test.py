#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016��5��18��

@author: li.taojun
'''
from config import render,urls
class Index:
    def GET(self):
        x = DataXing()
        y = DataXing(2,'testtitle','category','date')
        tls = [x,y]
        tpldata={}
        tpldata['posts'] = tls
        tpldata['totalpost'] = 20
        tpldata['pagestr'] = 'litaojun'
        return render.postlist(tpldata)
        #return render.index("")
class DataXing:
    def __init__(self,postid=1,posttitle = 'post_ti' ,postcategory = 'post_category',postdate = 'post_date'):
        self.post_title = posttitle
        self.post_category = postcategory
        self.post_date = postdate
        self.post_id = postid
        