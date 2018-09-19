# -*- coding: UTF-8 -*-
import re
from django.conf import settings
import cPickle as pickle
#
# dic = {'league': {},
#        'name': {},
#        'born': {},
#        'number': {},
#        'nba draft': {},
#        'nationality': {},
#        'position': {},
#        'education': {},
#        'career highlights and awards': {},
#        'died': {},
#        'allpro': {},
#        'last mlb appearance': {},
#        'teams': {},
#        'mlb debut': {},
#        }
# playerlist = []
# playerlist.append({})
# num = 0
# while num < 5052:
# 	num = num + 1
# 	path = 'D:/documents/Pythonapps/crawler/NBAtemp/' + repr(num)
# 	player = {}
# 	try:
# 		f = open(path, 'r')
# 	except IOError as err:
# 		playerlist.append(player)
# 		continue
# 	if 'nba' not in dic['league']:
# 		dic['league']['nba'] = set()
# 		dic['league']['nba'].add(repr(num))
# 	else:
# 		dic['league']['nba'].add(repr(num))
# 	src_data = f.readlines()
# 	for i in src_data:
# 		po = i.find('\t')
# 		th = i[0:po - 1].lower()
# 		td = i[po + 1:].strip().lower()
# 		u = set(re.split('[^A-Za-z0-9\._-]', td))
# 		if th == 'image':
# 			tp = re.search(r'\.\w+$', td).start() - len(td)
# 			tail = td[tp:]
# 			player['image'] = "images/" + str(num) + tail
# 			continue
# 		if td[0] == ';':
# 			td = td[1:]
# 		td.replace(';;', ';')
# 		if th == 'name':
# 			td = td.title()
# 		player[th] = td
# 		if '' in u:
# 			u.remove('')
# 		if th.find("name") != -1:
# 			th = "name"
# 		if th.find("osition") != -1:
# 			th = "position"
# 		if th.find("school") != -1 or th.find("ollege") != -1 or th.find("ducation") != -1:
# 			th = "education"
# 		if th.find("wards") != -1:
# 			th = "career highlights and awards"
# 		if th.find("bir") != -1:
# 			th = "born"
# 		if th.find("dea") != -1:
# 			th = "died"
# 		if th in dic:
# 			for j in u:
# 				if j not in dic[th]:
# 					dic[th][j] = set()
# 					dic[th][j].add(repr(num))
# 				else:
# 					dic[th][j].add(repr(num))
# 		for k in u:
# 			if k not in dic['allpro']:
# 				dic['allpro'][k] = set()
# 				dic['allpro'][k].add(repr(num))
# 			else:
# 				dic['allpro'][k].add(repr(num))
# 	playerlist.append(player)
# 	f.close()
#
# _num = 5052
# while num - _num < 6020:
# 	num = num + 1
# 	path = 'D:/documents/Pythonapps/crawler/MLBtemp/' + repr(num - _num)
# 	player = {}
# 	try:
# 		f = open(path, 'r')
# 	except IOError as err:
# 		playerlist.append(player)
# 		continue
# 	if 'mlb' not in dic['league']:
# 		dic['league']['mlb'] = set()
# 		dic['league']['mlb'].add(repr(num))
# 	else:
# 		dic['league']['mlb'].add(repr(num))
# 	src_data = f.readlines()
# 	for i in src_data:
# 		po = i.find('\t')
# 		th = i[0:po - 1].lower()
# 		td = i[po + 1:].strip().lower()
# 		u = set(re.split('[^A-Za-z0-9\._-]', td))
# 		if th == 'image':
# 			tp = re.search(r'\.\w+$', td).start() - len(td)
# 			tail = td[tp:]
# 			player['image'] = "images/" + str(num) + tail
# 			continue
# 		if th == 'type':
# 			continue
# 		if td[0] == ';':
# 			td = td[1:]
# 		td.replace(';;', ';')
# 		if th == 'name':
# 			td = td.title()
# 		player[th] = td
# 		if '' in u:
# 			u.remove('')
# 		if th.find("name") != -1:
# 			th = "name"
# 		if th.find("bir") != -1:
# 			th = "born"
# 		if th in dic:
# 			for j in u:
# 				if j not in dic[th]:
# 					dic[th][j] = set()
# 					dic[th][j].add(repr(num))
# 				else:
# 					dic[th][j].add(repr(num))
# 		for k in u:
# 			if k not in dic['allpro']:
# 				dic['allpro'][k] = set()
# 				dic['allpro'][k].add(repr(num))
# 			else:
# 				dic['allpro'][k].add(repr(num))
# 	playerlist.append(player)
# 	f.close()
# print dic.keys()
# print len(playerlist)
# out = open('D:/Program Files (x86)/python2.7/search/static/dic', 'wb')
# pickle.dump(dic, out, 2)
# out.close()
# _out = open('D:/Program Files (x86)/python2.7/search/static/playerlist', 'wb')
# pickle.dump(playerlist, _out, 2)
# _out.close()

