#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8') 

class GetMusic:
    
    def __init__(self):
        pass

    def getID(self, name):
        url = 'http://xxx.xxx.xxx.xxx/search?keywords=%s'%(name)
        data = requests.post(url)
        data = data.text.encode('utf-8')
        print (data.text)

if __name__ == "__main__":
    GetMusic().getID('海阔天空')

