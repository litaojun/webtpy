#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2016��5��18��

@author: li.taojun
'''
from config import render,urls
import config
import web
import httplib, urllib
import json
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
class OtherResouce:
    def GET(self):
        return render.index("meiyou")
class DealCode:
    def GET(self,code = 'litaojun'):
        retdata = "meiyou"
        curcode = web.input(code = 'test')
        curheader = web.cookies()
        print curheader
        print curcode.code
        print "code=%s" % code
        hearcookie = "Garfitle_session=%s" % curheader.Garfitle_session
        print "hearcookie=%s" % hearcookie
        paramjson = {}
        paramjson['client_id'] = 'm1'
        paramjson['client_secret'] = 's1'
        paramjson['grant_type'] = 'authorization_code'
        paramjson['redirect_uri'] = 'http://localhost:12345/litaojun'
        paramjson['code'] = curcode.code
        headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                    ,"Cookie":hearcookie
                    ,"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0"}
        print str(paramjson)
        params = urllib.urlencode(paramjson)
        print str(params)
        httpClient = httplib.HTTPConnection(config.hostip, config.port, timeout=30)
        httpClient.request("POST", "/appDemo/oauth/token", params,headers)
        response = httpClient.getresponse()
        #print response.status
        #print response.reason
        #print response.read()
        #print response.getheaders()
        if  response.status == 200:
            cookiejs = json.loads(response.read())
            print cookiejs
            retdata = cookiejs["access_token"]
        return render.indextest(retdata)
    
        