# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class WEATHER:

    def __init__(self):
        pass


    def getWeather(self):
        url = 'http://tianqi.moji.com/'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        date = re.compile('<ul class="days clearfix">.*?<a href.*?>(.*?)</a>.*?<img src.*?alt="(.*?)">.*?</span>.*?</li>.*?<li>(.*?) / (.*?)</li>.*?<li>.*?<em>(.*?)</em>.*?<b>(.*?)-(.*?)</b>.*?<strong.*?>(.*?)</strong>',re.S)
        return re.findall(date,content)

    def handleData(self):
        date = self.getWeather()
        C = []
        for d in date:
            C.append(d[0].encode('UTF-8'))
            C.append(d[1].encode('UTF-8'))
            C.append(d[2].encode('UTF-8'))
            C.append(d[3].encode('UTF-8'))
            C.append(d[4].encode('UTF-8'))
            C.append(d[5].encode('UTF-8'))
            C.append(d[6].encode('UTF-8'))
            C.append(d[7].encode('UTF-8'))
        return C 

    def results(self, day):
        C = self.handleData()
        if day == "1":
            return '主人，今天天气是' + C[1] + '，温度为' + C[2] + '到' + C[3] + '，' + C[4] + C[5] + '到' + C[6] + '，空气质量为' + C[7].strip()
        elif day == "2":
            return '主人，明天天气是' + C[9] + '，温度为' + C[10] + '到' + C[11] + '，' + C[12] + C[13] + '到' + C[14] + '，空气质量为' + C[15].strip()
        elif day == "3":
            return '主人，后天天气是' + C[17] + '，温度为' + C[18] + '到' + C[19] + '，' + C[20] + C[21] + '到' + C[22] + '，空气质量为' + C[23].strip()
        else:
            return "超出范围了"


if __name__ == '__main__':
    choice = raw_input(' >>>')
    print WEATHER().results(choice)
