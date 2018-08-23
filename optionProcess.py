#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing
import os
import psutil
from handle import HANDLE

class PROCESS:

    def __init__(self):
        self.h = HANDLE()


    def runNewProcess(self, _data):
        _newprocess = multiprocessing.Process(target=self.h.Start, args=(_data,))
        _newprocess.start()


    def killChilProcess(self, pid):
        _chidprocess =psutil.Process(pid).children()
        for i in _chidprocess:
            __pid = str(i)[16:-1].split(",")[0][3:]
            os.system("kill -9 %s"%(int(__pid)))


if __name__ == "__main__":
    p = PROCESS()
#    p.run()
#    p.run2()
#    while not q.empty():
#        print q.get()
#    p.ttt()
#    p.check()
    p.Start()
    getChilProcess(os.getpid())
    
#    print "done."
