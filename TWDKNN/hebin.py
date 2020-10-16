# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 12:20:16 2016

@author: ruikai
"""
# coding=utf-8
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 12:20:16 2016

@author: ruikai
"""
# coding=utf-8
import re
import os
import sys
import codecs
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')


def merge_file():
    path = "D:\ruikai\newname\jisuanji\\"
    resName = "D:\ruikai\hebing\jisuanji.txt"
    if os.path.exists(resName):
        os.remove(resName)
    result = codecs.open(resName, 'w', 'utf-8')

    num = 1
    while num <= 800:
        name = "%d" % num
        fileName = path + str(name) + ".txt"
        source = open(fileName, 'r')
        line = source.readline()
        line = line.strip('\n')
        line = line.strip('\r')

        while line != "":
            line = unicode(line, "utf-8")
            line = line.replace('\n', ' ')
            line = line.replace('\r', ' ')
            result.write(line + ' ')
            line = source.readline()
        else:
            print 'End file: ' + str(num)
            result.write('\n')
            source.close()
        num = num + 1

    else:
        print 'End All'
        result.close()


if __name__ == '__main__':
    merge_file()
