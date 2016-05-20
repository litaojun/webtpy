#!/usr/bin/env python
#coding=utf8
'''
Created on 2016��5��19��

@author: li.taojun
'''

 
import httplib, urllib
 
httpClient = None
try:
    params = urllib.urlencode({'name': 'tom', 'age': 22})
    headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/plain"}
 
    httpClient = httplib.HTTPConnection("localhost", 80, timeout=30)
    httpClient.request("POST", "/test.php", params, headers)
 
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() #��ȡͷ��Ϣ
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()