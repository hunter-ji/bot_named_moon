#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import random



class QiuShi:
    J = []

    def __init__(self):
        pass

    def run(self):
        replace_br = re.compile('<br/>')
        for num in range(1,30):
            url = 'https://www.qiushibaike.com/text/page/' + str(num) + '/?s=5001438'
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = { 'User-Agent' : user_agent }
            try:
                request = urllib2.Request(url,headers = headers)
                response = urllib2.urlopen(request)
                content = response.read().decode('utf-8')
                pattern = re.compile('<a class=.*?>.*?<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
                items = re.findall(pattern,content)
                for item in items:
                    ii = replace_br.sub("", item)
                    self.J.append(ii)
                n = random.randint(1,len(self.J))
                return self.J[n].strip()
            except urllib2.URLError, e:
                if hasattr(e,"code"):
                    print e.code
                if hasattr(e,"reason"):
                    print e.reason
                return "获取笑话失败"

if __name__ == '__main__':
    print QiuShi().run()

