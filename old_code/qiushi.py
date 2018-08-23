# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import random

def qiushi():
    J = []
    replace_br = re.compile('<br/>')
    n = random.randint(0,18)
    print n 

    url = 'http://www.qiushibaike.com'
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
            J.append(ii)

#            print L[n]
        return J[n]
#        print JOY[n]
#    print L[0]
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
            return e.code
        if hasattr(e,"reason"):
            print e.reason
            return e.reason

if __name__ == '__main__':
    qq = qiushi()
    print qq.encode('utf-8').strip()
