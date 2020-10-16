# -*- coding: utf-8 -*-
"""
@author: 芮凯
"""
import os
import fenci
import codecs
import pickle
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

def loadword(segPath,filename):
    (allfile, path) = fenci.getFileList('/Users/wyc/PycharmProjects/textclassificaton/text/muoxing/wordcount/huangjing')
    word = {}
    for ff in allfile:

        f = codecs.open(path + "/" + ff, 'rb', encoding='utf-8')
        l=0
        for line in f:
            #word = word + line.split()[0].split()
            key=line.split()[0]
            value=line.split()[1]

            word[key] = word.get(key, 0) + float(value)
            l=l+1
            if l > len(f.readlines())/2:

                break
        f.close()
        print word[1][0]
        print word[1][1]
        # 保存分词结果的目录

    if not os.path.exists(segPath):
            os.mkdir(segPath)

    # 将分词后的结果用空格隔开，保存至本地
    f = open(segPath + "/" + filename, "wb")
    for item in word:
        f.write('%s %s\n' % (item[0], item[1]))

    f.close()

if __name__ == "__main__":
    loadword("/Users/wyc/PycharmProjects/textclassificaton/text/muoxing/wordcount/merge" , "huangjing.txt")