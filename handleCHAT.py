#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sqlite3
import sys 
reload(sys)
sys.setdefaultencoding('utf-8') 


class handleChat:

    def __init__(self):
        self.conn = sqlite3.connect("thedata.db")

    def insertData(self, data):
        self.conn.execute("insert into chat (keywords, content) values ('%s','%s')"%(data[0],data[1]))
        self.conn.commit()

    def selectData(self, data):
        cur = self.conn.execute("select content from chat where keywords = '%s'"%(data))
        contents = [dict(content=row[0]) for row in cur.fetchall()]
        _len = len(contents)
        if _len != 1:
            L = {}
            for i in range(0,_len):
                L[i]=contents[i]['content']
            _num = random.randint(0,_len-1)
            return L[_num]
        return contents[0]['content']

    def deleteData(self, data):
        self.conn.execute("delete from chat where keywords = '%s'"%data)
        self.conn.commit()

if __name__ == "__main__":
#    data = str(raw_input(" >>>"))
    data = "你好"
    print handleChat().selectData(data)
#    a = raw_input(" >>>")
#    print a
    
