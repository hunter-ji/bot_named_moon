#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib, urllib2


class TuLing:

    def __init__(self):
        self.key = '0a28c4cae6f64be194c9acff663ee29b'

    def getHtml(self, url):
        page = urllib.urlopen(url)
        html = page.read()
        return html

    def Run(self, info):
        api = 'http://www.tuling123.com/openapi/api?key=' + self.key + '&info='
        request = api   + info
        response = self.getHtml(request)
        dic_json = json.loads(response)
        return dic_json['text']

if __name__ == "__main__":
    print TuLing().Run("嘿嘿".decode('utf-8'))
