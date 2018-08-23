#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import multiprocessing
from main import MAIN

class ProcessGuard:

    def __init__(self):
        self.main = multiprocessing.Process(target=self.Janet)

    def Janet(self):
        MAIN().Run()
        
    def Check(self):
        while True:
            if self.main.is_alive() == False:
                self.Start()
            time.sleep(5)
    
    def Start(self):
        self.main.start()


if __name__ == "__main__":
    p = ProcessGuard()
    p.Start()
    p.Check()
