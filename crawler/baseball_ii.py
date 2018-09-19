# -*- coding: UTF-8 -*-
import re

dic = {'allpro': {},
       'league': {},
       'last mlb appearance': {},
       'name': {},
       'teams': {},
       'mlb debut': {}
       }
num = 0
while num < 1000:
	num = num + 1
	path = './MLBtemp/' + repr(num)
	try:
		f = open(path, 'r')
	except IOError as err:
		print('File Error:' + str(err))
		continue
	if 'mlb' not in dic['league']:
		dic['league']['mlb'] = set(repr(num))
	else:
		dic['league']['mlb'].add(repr(num))
	src_data = f.readlines()
	for i in src_data:
		po = i.find('\t')
		th = i[0:po - 1].lower()
		td = i[po + 1:].strip().lower()
		u = set(re.split('[^A-Za-z0-9\._-]', td))
		if th == 'image' or th == 'type':
			continue
		if '' in u:
			u.remove('')
		if th.find("name") != -1:
			th = "name"
		# if th.find("osition") != -1:
		# 	th = "position"
		# if th.find("school") != -1 or th.find("ollege") != -1 or th.find("ducation") != -1:
		# 	th = "education"
		# if th.find("wards") != -1:
		# 	th = "career highlights and awards"
		if th.find("bir") != -1:
			th = "born"
		# if th.find("dea") != -1:
		# 	th = "died"
		if th  in dic:
			for j in u:
				if j not in dic[th]:
					dic[th][j] = set(repr(num))
				else:
					dic[th][j].add(repr(num))
		for k in u:
			if k not in dic['allpro']:
				dic['allpro'][k] = set(repr(num))
			else:
				dic['allpro'][k].add(repr(num))
	f.close()
