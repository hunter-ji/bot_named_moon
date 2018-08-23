#!/usr/bin/python
# -*- coding:utf-8 -*-
import wave
import urllib, urllib2, pycurl
import base64
import json
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


from gettext import get_token

'''
def get_token():
    apiKey = "GM75YwcRmCtbAZQKoaBfKmSN"
    secretKey = "b03d191ee8dc072d1972d0d98896f0e7" 
    auth_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=" + apiKey + "&client_secret=" + secretKey;
    res = urllib2.urlopen(auth_url)
    json_data = res.read()
    return json.loads(json_data)['access_token']
'''

def get_voice(token, text):
    cuid = '9619749'
    getvoice_url = 'http://tsn.baidu.com/text2audio?tex=' + text + '&lan=zh&cuid=' + cuid + '&ctp=1&tok=' + token + '&per=4'
    req = urllib2.urlopen(getvoice_url)
    res = req.read()
    voice = open('.1.mp3','wb+')
#    print type(voice)
    voice.write(res)
#    print type(voice)
    voice.close()

def play_voice():
    os.system('mplayer .1.mp3')
#    os.system('rm "%s" -f'%filename)


if __name__ == '__main__':
    token = get_token()
    text = raw_input(u'Please enter :')
    get_voice(token, text)
    play_voice()





