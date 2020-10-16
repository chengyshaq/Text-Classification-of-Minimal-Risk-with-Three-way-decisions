# -*- coding: utf-8 -*-
"""
@author: 芮凯
"""
import os
import fenci
import codecs
import algorithm1
import algorithm2
import wordcount
import sys
reload(sys)

sys.setdefaultencoding('utf-8')

if __name__ == "__main__":

#*************************************修改参数区域***************************************************
    # 需要分类的文件目录
    sourcePath = 'd:/newruikai/ceshiji'
    #分词后的目录
    fencPath= 'd:/newruikai/fencihou'
    #词频统计目录
    wcPath= 'd:/newruikai/cipincount'
    #五大类词频统计结果
    typePath = 'd:/newruikai/5lei'
    #最终结果路径
    resultPath = 'd:/newruikai/zuihou'
    pp=2
    pn=4
    bp=2.54
    bn=2.54
    np=3
    nn=4
    #预估结果
    forecast="art"
#*****************************************************************************************************


    sourcecnt=0
    truecnt=0
    filecnt=0
    algorithm2cnt=0
    (allfile, path) = fenci.getFileList(sourcePath)
    for ff in allfile:
        sourcecnt = sourcecnt+1
        result=''
        fenci.fenci(ff, path, fencPath)
        wordcount.wordcount(ff, fencPath, wcPath)
        #算法1
        (allfile1, path1) = fenci.getFileList(typePath)
        bnd={}
        pos ={}
        algorithm2s={}
        for ff1 in allfile1:
            desword = algorithm1.loaddes(ff1, path1)
            word = algorithm1.loadword(ff, wcPath)
            tf = algorithm1.TF(word, desword, "500")
            (idf, rap, ran) = algorithm1.IDF(pp, pn, bp, bn, np, nn, tf)
            print ff1 + "  " + idf + "  " + str(tf) + " " + str(rap) + " " + str(ran)
            algorithm2s[str(ff1).split('.')[0]] = rap
            if idf == "bnd":
                bnd[str(ff1).split('.')[0]]=rap

            if idf == "pos":
                pos[str(ff1).split('.')[0]]=rap
        if len(pos) == 0:
            #算法2
            algorithm2cnt = algorithm2cnt +1
            type = {}
            for ff2 in allfile1:
                word1 = algorithm2.loaddes(ff2, path1)
                word2 = algorithm2.loadword(ff,wcPath)
                cosnum = algorithm2.MergeKeys(word1, word2)
                type[str(ff2).split('.')[0]] = cosnum
            result= max(type.items(), key=lambda x: x[1])[0]

        else:
            result= min(algorithm2s.items(), key=lambda x: x[1])[0]
        if result !=forecast:
            filecnt = filecnt +1
        else:
            truecnt = truecnt +1

        # 将结果用空格隔开，保存至本地
        f = open(resultPath + "/" + result+".txt", "a")
        f.write('%s\n' % (ff))

        f.close()

    print  "处理文件总数"+str(sourcecnt)
    print  "分类正确文件个数"+str(truecnt)
    print  "分类失败文件个数"+str(filecnt)
    print  "使用算法2处理文件个数"+str(algorithm2cnt)
