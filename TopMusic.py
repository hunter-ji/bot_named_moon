# -*- coding:utf-8 -*-
import urllib
import urllib2
import re


class TOPMusic:

    def __init__(self):
        self.url = "http://music.baidu.com/tag/"
    
    def getTop(self, _type):
       
        url = self.url + _type
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        try:
            request = urllib2.Request(url,headers = headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            pattern = re.compile('<span class="song-title".*?>(.*?)</span>',re.S)
            items = re.findall(pattern,content)
            new_page = "".join(items)
            get_title = re.compile('<a href=.*?>(.*?)</a>')
            itemss = re.findall(get_title, new_page)
#            print ",".join(itemss)
            return itemss
        except urllib2.URLError, e:
            return "error"

    def playTop(self,_type):
        data = self.getTop(_type)
        if data != "error":
            n = 0
            L = {}
            for i in data:
                L[n]=i
                n += 1
            return L
        else:
            return "error"
    
    def showTop(self,_type):
        data = self.getTop(_type)
        if data != "error":
            data = data[:5]
            return "主人,推荐%s音乐排行榜前五首是,"%(_type) + ",".join(data).encode('utf-8')
        else:
            return "error"


if __name__ == "__main__":
    _type = raw_input('>>>')
    print TOPMusic().showTop(_type)
