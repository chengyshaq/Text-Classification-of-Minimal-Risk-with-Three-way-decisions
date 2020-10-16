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
def wordcount(filename,path,segPath):
    wordc = []
    wordMap = {}
    f = codecs.open(path + "/" + filename, 'rb', encoding='utf-8')
    for line in f:
        wordc= wordc+line.split()
    f.close()
    for word in wordc:
        wordMap[word] = wordMap.get(word, 0) + 1

    sortedNewWordMap = sorted(wordMap.iteritems(), key=lambda asd:asd[1], reverse=True)
    print sortedNewWordMap



    # 保存分词结果的目录

    if not os.path.exists(segPath):
        os.mkdir(segPath)

    # 将分词后的结果用空格隔开，保存至本地
    f = open(segPath + "/" + filename , "wb")
    for item in sortedNewWordMap:
        f.write('%s %.1f\n' % (item[0], item[1]))

    f.close()



if __name__ == "__main__":
	#保存词频的目录
	segPath = 'd:/newruikai/cipincount'
	(allfile,path) = fenci.getFileList('d:/newruikai/fencihou')
	for ff in allfile:
		print "Using jieba on " + ff
		wordcount(ff,path,segPath)
