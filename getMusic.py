#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import re,os
import json
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class GetMusic:

    def __init__(self):
        pass

    def getID(self, name):
        name = urllib.quote(name)
        url = 'http://xxx.xxx.xxx.xxx/search?keywords=%s'%(name)
        print url, '\n'
        req = urllib2.Request(url)
        con = urllib2.urlopen(req).read()
        print type(con)
        decoded = json.loads(con)
        #print decoded
        return decoded['result']['songs'][0]['id']

    def PlaySong(self, id):
#        id = self.getID(name)
        url = 'http://the_ip:3000/music/url?id=%s'%(id)
        req = urllib2.Request(url)
        con = urllib2.urlopen(req).read()
        data = json.loads(con)
        playSongUrl = data['data'][0]['url']
        print playSongUrl
        os.system('mplayer "%s"'%playSongUrl)

if __name__ == "__main__":
    name = '海阔天空'
    name = urllib.quote(name)
    g = GetMusic()
    id = g.getID(name)
    g.PlaySong(id)
