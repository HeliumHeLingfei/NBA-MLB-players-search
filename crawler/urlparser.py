# -*- coding: UTF-8 -*-
# import urllib2
# import urllib
# from urllib2 import HTTPError
# from bs4 import BeautifulSoup
# import cPickle as pickle
# import re
#
# url = 'https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_players_(F)'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = {'User-Agent': user_agent}
# values = {'q': 'python'}
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(req)
# the_page = response.read()
# soup = BeautifulSoup(the_page, 'lxml')
#
# playerlist = []
# num = 0
# p = soup.find_all("div", class_="div-col columns column-count column-count-3")
# for k in p:
# 	for j in k.find_all('li'):
# 		h = j.a['href']
# 		print h
# 		temp_url = "https://en.wikipedia.org" + h
# 		# pattern = re.compile(r'.*(?=_\((\w+)\))')
# 		# b = re.search(pattern, h)
# 		# if b:
# 		# 	temp_url = "https://en.wikipedia.org" + b.group()
# 		# 	temp_soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(temp_url, data, headers)).read(), 'lxml')
# 		# 	q = temp_soup.find_all("div", class_="mw-parser-output")
# 		# 	pattern2 = re.compile(r' may refer to\:\<\/p\>')
# 		# 	t=repr(q[0].p)
# 		# 	d = re.search(pattern2, t)
# 		# 	if d:
# 		# 		print b.group()
# 		# 		for v in q[0].find_all('li'):
# 		# 			if v.has_attr('class'):
# 		# 				continue
# 		# 			playerlist.append("https://en.wikipedia.org" + v.a['href'])
# 		# 			num = num + 1
# 		# 	else:
# 		# 		playerlist.append(temp_url)
# 		# 		num = num + 1
# 		# 		temp_url = "https://en.wikipedia.org" + h
# 		# 		playerlist.append(temp_url)
# 		# 		num = num + 1
# 		# else:
# 		playerlist.append(temp_url)
# 		num = num + 1
# 		print num
#
# inp = open('MLBplayerslist', 'r')
# players = pickle.load(inp)
# players.extend(playerlist)
# inp.close()
#
# output = open('MLBplayerslist', 'w')
# pickle.dump(players, output)
# output.close()



# #
# # -*- coding: UTF-8 -*-
# import urllib2
# import urllib
# from urllib2 import HTTPError
# from bs4 import BeautifulSoup
# import cPickle as pickle
# import re
#
# url = 'https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_players_(G)'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = {'User-Agent': user_agent}
# values = {'q': 'python'}
# data = urllib.urlencode(values)
# req = urllib2.Request(url, data, headers)
# response = urllib2.urlopen(req)
# the_page = response.read()
# soup = BeautifulSoup(the_page, 'lxml')
#
# playerlist = []
# num = 0
# p = soup.find_all("div", class_="mw-parser-output")
# for k in p:
# 	for j in k.find_all('ul')[1].find_all('li'):
# 		h = j.a['href']
# 		print h
# 		temp_url = "https://en.wikipedia.org" + h
# 		# pattern = re.compile(r'.*(?=_\((\w+)\))')
# 		# b = re.search(pattern, h)
# 		# if b:
# 		# 	temp_url = "https://en.wikipedia.org" + b.group()
# 		# 	temp_soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(temp_url, data, headers)).read(), 'lxml')
# 		# 	q = temp_soup.find_all("div", class_="mw-parser-output")
# 		# 	pattern2 = re.compile(r' may refer to\:\<\/p\>')
# 		# 	t=repr(q[0].p)
# 		# 	d = re.search(pattern2, t)
# 		# 	if d:
# 		# 		print b.group()
# 		# 		for v in q[0].find_all('li'):
# 		# 			if v.has_attr('class'):
# 		# 				continue
# 		# 			playerlist.append("https://en.wikipedia.org" + v.a['href'])
# 		# 			num = num + 1
# 		# 	else:
# 		# 		playerlist.append(temp_url)
# 		# 		num = num + 1
# 		# 		temp_url = "https://en.wikipedia.org" + h
# 		# 		playerlist.append(temp_url)
# 		# 		num = num + 1
# 		# else:
# 		playerlist.append(temp_url)
# 		num = num + 1
# 		print num
#
# inp = open('MLBplayerslist', 'r')
# players = pickle.load(inp)
# players.extend(playerlist)
# inp.close()
#
# output = open('MLBplayerslist', 'w')
# pickle.dump(players, output)
# output.close()


#
# -*- coding: UTF-8 -*-
import urllib2
import urllib
from urllib2 import HTTPError
from bs4 import BeautifulSoup
import cPickle as pickle
import re

url = 'https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_players_(Wa%E2%80%93Wh)'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
values = {'q': 'python'}
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()
soup = BeautifulSoup(the_page, 'lxml')
playerlist = []
num = 0
p = soup.find_all('tr')
boo = 0
for j in p:
	if boo == 0:
		boo = 1
		continue
	h = j.td.a['href']
	print h
	temp_url = "https://en.wikipedia.org" + h
	# pattern = re.compile(r'.*(?=_\((\w+)\))')
	# b = re.search(pattern, h)
	# if b:
	# 	temp_url = "https://en.wikipedia.org" + b.group()
	# 	temp_soup = BeautifulSoup(urllib2.urlopen(urllib2.Request(temp_url, data, headers)).read(), 'lxml')
	# 	q = temp_soup.find_all("div", class_="mw-parser-output")
	# 	pattern2 = re.compile(r' may refer to\:\<\/p\>')
	# 	t=repr(q[0].p)
	# 	d = re.search(pattern2, t)
	# 	if d:
	# 		print b.group()
	# 		for v in q[0].find_all('li'):
	# 			if v.has_attr('class'):
	# 				continue
	# 			playerlist.append("https://en.wikipedia.org" + v.a['href'])
	# 			num = num + 1
	# 	else:
	# 		playerlist.append(temp_url)
	# 		num = num + 1
	# 		temp_url = "https://en.wikipedia.org" + h
	# 		playerlist.append(temp_url)
	# 		num = num + 1
	# else:
	playerlist.append(temp_url)
	num = num + 1
	print num
inp = open('MLBplayerslist', 'r')
players = pickle.load(inp)
players.extend(playerlist)
inp.close()

output = open('MLBplayerslist', 'w')
pickle.dump(players, output)
output.close()
