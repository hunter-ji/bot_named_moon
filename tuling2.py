#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests
import sys
reload(sys) 
sys.setdefaultencoding( "utf-8" )

def tuling(message):
    data = {'key':'cc3903d397e54a3e9c984635269e7643', 'info':message, 'userid':'123456'}
    url = 'http://www.tuling123.com/openapi/api'
    r = requests.post(url, data=data)
    mes = json.loads(r.text)
    return mes['text'].encode('utf-8')

if __name__ == '__main__':
        print tuling('你好'.encode('utf-8'))
