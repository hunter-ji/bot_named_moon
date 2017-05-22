# -*- coding:utf-8 -*-
n = 0
import urllib
import urllib2
import re
import random




def weather():
    C = []
    url = 'http://tianqi.moji.com/'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    date = re.compile('<ul class="days clearfix">.*?<a href.*?>(.*?)</a>.*?<img src.*?alt="(.*?)">.*?</span>.*?</li>.*?<li>(.*?) / (.*?)</li>.*?<li>.*?<em>(.*?)</em>.*?<b>(.*?)-(.*?)</b>.*?<strong.*?>(.*?)</strong>',re.S)
    date_l = re.findall(date,content)
    return date_l



if __name__ == '__main__':
    weather()

