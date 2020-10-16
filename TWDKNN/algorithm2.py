# -*- coding: utf-8 -*-
"""
@author: 芮凯
"""
import os
import fenci
import codecs
import math
import sys
reload(sys)

sys.setdefaultencoding('utf-8')


def loadword(filename,path):
    f = codecs.open(path + "/" + filename, 'rb', encoding='utf-8')
    lines=f.readlines()
    f.close()
    num=len(lines)/2
    word = dict([(line.split()[0], float(line.split()[1])) for line in lines[:num]])
    return word

def loaddes(filename,path):
    word = {}
    f = codecs.open(path + "/" + filename, 'rb', encoding='utf-8')
    for line in f:

      key = line.split(',')[0]
      value = line.split(',')[1]
      word[key] = word.get(key, 0) + float(value)
    f.close()
    return word

def MergeKeys(dic1,dic2):
    arrayKey = []
    for key in dic1:
        arrayKey.append(key)
    for key in dic2:
        if key in arrayKey:
            continue
        else:
            arrayKey.append(key)

    # 计算词频
    arrayNum1 = [0] * len(arrayKey)
    arrayNum2 = [0] * len(arrayKey)

    arrayKey_map = {}
    for index, array_value in enumerate(arrayKey):
        arrayKey_map[array_value] = index
    #支持度
    zcdfz=0
    zcdfm=0
    # 赋值arrayNum1
    for key, value in dic1.iteritems():
        # value = dic1[key]
        # j = 0
        if key in arrayKey_map:
            arrayNum1[arrayKey_map[key]] = value
        zcdfz=zcdfz+value
    # 赋值arrayNum2
    for key, value in dic2.iteritems():
        if key in arrayKey_map:
            arrayNum2[arrayKey_map[key]] = value
            zcdfm =zcdfm+value

    # 计算两个向量的点积
    x = 0
    i = 0
    sq1 = 0
    sq2 = 0
    leng = len(arrayKey)
    while i < leng:
        x = x + arrayNum1[i] * arrayNum2[i]
        # 计算两个向量的模
        sq1 = sq1 + arrayNum1[i] * arrayNum1[i]  # pow(a,2)
        sq2 = sq2 + arrayNum2[i] * arrayNum2[i]
        i = i + 1
    result = float(x) / (math.sqrt(sq1) * math.sqrt(sq2))
    #支持度
    zcd=zcdfz/zcdfm
    return result*zcd



if __name__ == "__main__":
    type={}
    (allfile,path) = fenci.getFileList('d:/newruikai/4lei')
    for file in allfile:
        word1=loaddes(file, path)
        word2 = loadword('1.txt','D:/newruikai/ceshis/count')
        cosnum = MergeKeys(word1,word2)
        type[str(file).split('.')[0]] = cosnum
    print max(type.items(), key=lambda x: x[1])[0]

