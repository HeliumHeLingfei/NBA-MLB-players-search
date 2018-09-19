# -*- coding: UTF-8 -*-
# import re
#
# pattern = re.compile(r'.*(?=_\((\w+)\))')
# a = re.search(pattern, '/wiki/Bill_Meyer_(basketball)')
# print a.group()
#
# pattern2 = re.compile(r' may refer to\:\<\/p\>')
# b = re.search(pattern2, '<p><b>Corey Williams</b> may refer to:</p>')
# print b.group()
import sys

reload(sys)
sys.setdefaultencoding('utf8')

num = 1
import cPickle as pickle
import re

pattern = re.compile(r'Batted:')
pattern2 = re.compile(r'Threw:')
while num < 5074:
	try:
		f = open('./MLBtemp/' + repr(num), 'r')
	except IOError as err:
		print('File Error:' + str(err))
		num=num+1
		continue
	print num
	dic = pickle.load(f)
	f.close()
	inp = open('./MLB/' + repr(num), 'w+')
	st = ""
	for i in dic.keys():
		if len(dic[i]) == 0:
			continue
		for j in dic[i]:
			if i == "name" or i == "image":
				st = st + j
			else:
				st = st + " " + j
		nu = 0
		for th in pattern2.finditer(st):
			nu = nu + 1
			if nu > 1:
				st = st[0:th.start()]
				break
		nu = 0
		for ba in pattern.finditer(st):
			nu = nu + 1
			if nu > 1:
				st = st[0:ba.start()]
				break
		st = i + "$" + "\t" + st + "\n"
		inp.write(st.encode('utf-8'))
		st = ""
	inp.close()
	num = num + 1



# print "value"
# for i in dic.keys():
# 	if len(dic[i])==0:
# 		continue
# 	for j in dic[i]:
# 		st = st + j
# 	print st
# 	st = ""
#
# print "key"
# for i in dic.keys():
# 	if len(dic[i])==0:
# 		continue
# 	print i
