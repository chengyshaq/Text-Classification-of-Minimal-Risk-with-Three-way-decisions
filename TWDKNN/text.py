# -*- encoding:utf-8 -*-
#******************文章去掉非特征词******************* 
def train_drop_otherword():         #训练文本
	f=open("corpus_train_drop_use.txt","w")
	fr=open("feature_word.txt","r")
	words=fr.readlines()
	keyword=set()
	for word in words:
		keyword.add(word.strip())
	frr=open("corpus_train.txt","r")
	lines=frr.readlines()
	for line in lines:
		line = line.strip().split(" ")
		f.write(line[0]+" ")
		for i in range(1,len(line)):
			if line[i] in keyword:
				f.write(line[i]+" ")
		f.write("\n")

def test_drop_otherword():
	f=open("corpus_test_drop_use.txt","w")
	fr=open("feature_word.txt","r")
	words=fr.readlines()
	keyword=set()
	for word in words:
		keyword.add(word.strip())
	frr=open("corpus_test.txt","r")#测试集
	lines=frr.readlines()
	for line in lines:
		line = line.strip().split(" ")
		f.write(line[0]+" ")
		for i in range(1,len(line)):
			if line[i] in keyword:
				f.write(line[i]+" ")
		f.write("\n")

import time

def loaddata():
	fr_train_read=open("corpus_train_drop_use.txt","r")
	fr_test_read=open("corpus_test_drop_use.txt","r")
	label_train=[]
	sentences_train=[]#训练集读入	
	lines_train=fr_train_read.readlines()
	for line_sentence in lines_train:
		line=[]
		if " "  in line_sentence.strip():
			line=line_sentence.strip().split(" ",1)
		else:
			line.append(line_sentence.strip())
			line.append("")
		if line[0]=="Auto":
			label_train.append(0)
		elif line[0]=="Culture":
			label_train.append(1)
		elif line[0]=="Economy":
			label_train.append(2)
		elif line[0]=="Medicine":
			label_train.append(3)
		elif line[0]=="Military":
			label_train.append(4)
		elif line[0]=="Sports":
			label_train.append(5)
		else:
			pass
		sentences_train.append(line[1])


	label_test=[]
	sentences_test=[]#测试集读入
	lines_test=fr_test_read.readlines()
	for line_sentence in lines_test:
		line=[]
		if " " in line_sentence.strip():
			line=line_sentence.strip().split(" ",1)
		else:
			line.append(line_sentence.strip())
			line.append("")
		if line[0]=="Auto":
			label_test.append(0)
		elif line[0]=="Culture":
			label_test.append(1)
		elif line[0]=="Economy":
			label_test.append(2)
		elif line[0]=="Medicine":
			label_test.append(3)
		elif line[0]=="Military":
			label_test.append(4)
		elif line[0]=="Sports":
			label_test.append(5)
		else:
			pass
		sentences_test.append(line[1])
	return sentences_train,label_train,sentences_test,label_test
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
def tfidf():
	sentences_train,labels_train,sentences_test,labels_test=loaddata()
	tfidf_vectorizer=TfidfVectorizer(token_pattern=u'(?u)\\b\\w+\\b',min_df=1)
	tfidf_matrix=tfidf_vectorizer.fit_transform(sentences_train)
	word=tfidf_vectorizer.get_feature_names()
	weight_train=tfidf_matrix.toarray()
	print "特征词个数:",
	print len(word)
	'''st=""
	for i in tfidf_vectorizer.vocabulary_:	#打印特征词
		st+=" "+i
	print st
	'''
	new_term_freq_matrix=tfidf_vectorizer.transform(sentences_test)
	weight_test=new_term_freq_matrix.toarray()
	return weight_train,labels_train,weight_test,labels_test,1200

from sklearn.neighbors import KNeighborsClassifier#分类模型
def knn():
	weight_train,labels_train,weight_test,label_test,choice_need=tfidf()
	start=time.clock()	
	neigh=KNeighborsClassifier(n_neighbors=30)
	neigh.fit(weight_train,labels_train)
	
	knn_result=neigh.predict(weight_test)
	knn_right=knn_wrong=0
	right_0=right_1=right_2=right_3=right_4=right_5=0
	wrong_0=wrong_1=wrong_2=wrong_3=wrong_4=wrong_5=0
	back_0=back_1=back_2=back_3=back_4=back_5=0
	for i in range(len(knn_result)):
		if knn_result[i]==0:
			back_0=back_0+1
		elif knn_result[i]==1:
			back_1=back_1+1
		elif knn_result[i]==2:	
			back_2=back_2+1
		elif knn_result[i]==3:
			back_3=back_3+1
		elif knn_result[i]==4:
			back_4=back_4+1
		elif knn_result[i]==5:
			back_5=back_5+1


		if knn_result[i]==label_test[i]:
			knn_right=knn_right+1
			if knn_result[i]==0 and label_test[i]==0:
				right_0=right_0+1
			elif knn_result[i]==1 and label_test[i]==1:
				right_1=right_1+1
			elif knn_result[i]==2 and label_test[i]==2:
				right_2=right_2+1
			elif knn_result[i]==3 and label_test[i]==3:
				right_3=right_3+1
			elif knn_result[i]==4 and label_test[i]==4:
				right_4=right_4+1
			elif knn_result[i]==5 and label_test[i]==5:
				right_5=right_5+1
		else:
			pass
	print "测试文档总数:",
	print len(label_test)
	print"正确分类的总文档:",
	print knn_right
	print "各类正确文档数:",
	print right_0,right_1,right_2,right_3,right_4,right_5
	wrong_0=len(label_test)/6-right_0
	wrong_1=len(label_test)/6-right_1
	wrong_2=len(label_test)/6-right_2
	wrong_3=len(label_test)/6-right_3
	wrong_4=len(label_test)/6-right_4
	wrong_5=len(label_test)/6-right_5
	print "各类错分文档数:",
	print wrong_0,wrong_1,wrong_2,wrong_3,wrong_4,wrong_5
	print "各类召回文档数:",
	print back_0,back_1,back_2,back_3,back_4,back_5
	p0=float(right_0)/(len(label_test)/6)
	p1=float(right_1)/(len(label_test)/6)
	p2=float(right_2)/(len(label_test)/6)
	p3=float(right_3)/(len(label_test)/6)
	p4=float(right_4)/(len(label_test)/6)
	p5=float(right_5)/(len(label_test)/6)
	r0=float(right_0)/back_0
	r1=float(right_1)/back_1
	r2=float(right_2)/back_2
	r3=float(right_3)/back_3
	r4=float(right_4)/back_4
	r5=float(right_5)/back_5
	print "每个类准确率:",
	print p0,p1,p2,p3,p4,p5
	print "每个类召回率:",
	print r0,r1,r2,r3,r4,r5
	f0=float(2*r0*p0)/(r0+p0)
	f1=float(2*r1*p1)/(r1+p1)
	f2=float(2*r2*p2)/(r2+p2)
	f3=float(2*r3*p3)/(r3+p3)
	f4=float(2*r4*p4)/(r4+p4)
	f5=float(2*r5*p5)/(r5+p5)
	print "每个类f值:",
	print f0,f1,f2,f3,f4,f5
	m_p=float(p0+p1+p2+p3+p4+p5)/6
	m_r=float(r0+r1+r2+r3+r4+r5)/6
	m_f=float(2*m_p*m_r)/(m_p+m_r)
	print "平率准确率，召回率，f值:",	
	print m_p,m_r,m_f
	end=time.clock()
	print "分类时间:"+str(end-start)+" s"
if __name__=="__main__":
	train_drop_otherword()
	test_drop_otherword()
	knn()
