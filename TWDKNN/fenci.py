# -*- coding: utf-8 -*-
"""
@author: 芮凯
"""

import os
import jieba
import sys
import re
import jieba.analyse
import string

reload(sys)

sys.setdefaultencoding('utf-8')



def __init__(name, gender, birth):
	jieba.load_userdict("D://ceshi/xiandai.dict")

def getFileList(path):
	filelist = []
	files = os.listdir(path)
	for f in files:
		if f[0] == '.':
			pass
		else:
			filelist.append(f)
	return filelist,path


def fenci(filename,path,segPath):
	f = open(path +"/" + filename,'r+')
	file_list = f.read()
	f.close()

	 #保存分词结果的目录

	if not os.path.exists(segPath):
		os.mkdir(segPath)

	#对文档进行分词处理

	print (u'正在进行分词......')
	seg_list = jieba.cut(file_list,cut_all=False)

	stopwords= [line.strip().decode('utf-8') for line in open('D://ruikai/newhgd.txt').readlines()]
	result = []

	deEstr = string.punctuation + ' ' + string.digits + string.letters
	deCstr = '，。《》【】（）！？★”“、：…〔〕＊「」；○ ◆ ～ ．％ ° ［ ］′ × ＜ ó í ó ° á é ● ∶＠ ⑴ ⑵ ⑶ ≤ ∈ σ φ  Φ 〈  〈 ＝ － #$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~'
	destr = deEstr + deCstr
	for seg in seg_list:
		seg = ''.join(set(seg.split())-set(stopwords))
		reg = '[a-zA-Z0-9]+'
		r = re.search(reg,seg)
		if seg  not in destr and not r  :
			result.append(seg)
	print (u'分词完成......')
	print (u'正在过滤停用词......')

	print (u'过滤停用词完成......')



	#将分词后的结果用空格隔开，保存至本地
	f = open(segPath+"/"+filename ,"w+")
	f.write(' '.join(result))
	f.close()


if __name__ == "__main__":
	#保存分词的目录
	segPath = 'd:/newruikai/fencihou'

	(allfile,path) = getFileList('D://newruikai/ceshiji')
	for ff in allfile:
		print "Using jieba on " + ff
		fenci(ff,path,segPath)

