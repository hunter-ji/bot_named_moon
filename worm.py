#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import requests
import random
import sys
reload(sys) 
sys.setdefaultencoding( "utf-8" )

class WORM:

    def __init__(self):
        self.url = 'http://jandan.net/duan'

    def worm(self):
        headers = {
                'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.52' 
                }
        response = requests.get(self.url, headers=headers)
        html = response.text
        pattern = re.compile('</span><p>(.*?)</p>', re.S)
        data = pattern.findall(html)
        data2 = self.getrandom(data)
        return self.tool(data2).encode('utf-8')

    def tool(self, x):
        removeBR = re.compile('<br>|<br />')
        x = re.sub(removeBR, '', x)
        x = x.replace('\n', '')
        return x.strip()

    def getrandom(self, data):
        thelen = len(data)-1
        n = random.randint(0, thelen) 
        return data[n]

if __name__ == '__main__':
    w = WORM()
    a = w.worm()
    print a
