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

def loadword(filename,path):
    word = []
    f = codecs.open(path + "/" + filename, 'rb', encoding='utf-8')
    for line in f:
        word = word + line.split()[0].split()
    f.close()
    return word

def loaddes(filename,path):
    word = []
    f = codecs.open(path + "/" + filename, 'rb', encoding='utf-8')
    for line in f:
      #  wordMap = wordMap.get(line.split(',')[0], line.split(',')[1])
      word = word + line.split(',')[0].split()


    f.close()

    return word

def TF(word,deswod,num):
    newword = word[0: int(num)]

    return  len(set(deswod).intersection(set(newword)))/float(600)

def IDF(pp,pn,bp,bn,np,nn,tf):
    rap= pp * tf + pn * (1 - tf)
    rab = bp * tf + bn * (1 - tf)
    ran = np * tf + nn * (1 - tf)

    if rap <= rab and rap <= ran:
        return ("pos", rap,ran)
    if ran <= rap and ran <=rab:
        return ("neg",rap,ran)
    if rab <= rap and rab <= ran:
        return ("bnd",rap,ran)

if __name__ == "__main__":
    pp=2
    pn=4
    bp=2.54
    bn=2.54
    np=3
    nn=4
	#保存词频的目录
    (allfile,path) = fenci.getFileList('d:/newruikai/5lei')
    for ff in allfile:
        desword =loaddes(ff, path)
        (all, p) = fenci.getFileList('d:/newruikai/test')
        posn=0
        for f in all:
            word = loadword(f, p)
            tf = TF(word,desword, 600)
            (idf, rap, ran) = IDF(pp, pn, bp, bn, np, nn, tf)
            print ff + "  " + idf + "  " + str(tf) + " "+ "Rap:" + str(rap)+ " "+"Ran:" + str(ran)


