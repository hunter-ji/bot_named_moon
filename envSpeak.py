#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
from multiprocessing import Process

from ok import GetAudio
GetAudio().Run() 

class EnvSpeak:

    def __init__(self):
        self.p = Process(target=self.__Run)

    def setAudio(self, num):
        os.system("amixer -c 1 cset numid=6,iface=MIXER,name='L ADC VOLUME' %s"%(num))

    def __getAudio(self):
        GetAudio().Run() 

    def __Start(self):
        p.start()

    def __Run(self):
        self.setAudio(0)
        self.__getAudio()
        self.setAudio(25)

    def __Checking(self):
        self.__Start()
        alive = self.p.is_alive()
        while True:
            if alive == False:
                break
            time.sleep(1)

if __name__ == "__main__":
    pass
