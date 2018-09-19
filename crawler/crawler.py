# -*- coding: UTF-8 -*-
import urllib2
import urllib
from urllib2 import HTTPError,URLError
from bs4 import BeautifulSoup
import cPickle as pickle
import re
import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')

sys.setrecursionlimit(1000000)  # 例如这里设置为一百万

num = 4999
total = 0
inp = open('NBAplayerslist', 'r')
players = pickle.load(inp)
inp.close()
dic = {}
tem = []
th = ''

while num < 5052:
	url = players[num]
	num = num + 1
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = {'User-Agent': user_agent}
	values = {'q': 'python'}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data, headers)
	try:
		response = urllib2.urlopen(req)
	except HTTPError or URLError:
		continue
	the_page = response.read()
	soup = BeautifulSoup(the_page, 'lxml')
	infobox = soup.find_all('table', class_="infobox vcard")
	if not infobox:
		continue
	if infobox[0].find(class_='image'):
		image = infobox[0].find(class_='image')['href']
		dic['image'] = image

	trs = infobox[0].find_all('tr')
	k = 0
	for i in trs:
		tds = i.find_all(['td', 'th', 'li'])
		if not tds:
			continue
		for j in tds:
			if j.name == 'th':
				# if j.string == "Career highlights and awards":
				# 	print "break"
				# 	break
				k = 1
				th = ""
				for _s in j.stripped_strings:
					th = th + _s
				dic[th] = []
			else:
				if j.find_all('ul') or not k == 1:
					continue
				temps=""
				for s in j.stripped_strings:
					temps=temps+s.replace(u"\xa0", u"").replace(u"\u2013", u"-")
				dic[th].append(temps+";")

	pattern = re.compile(r'(?<=/wiki/).*(?=_\((.*)\))')
	pattern2 = re.compile(r'(?<=/wiki/).*')
	pattern3 = re.compile(r'(?<=title=).*(?=&action)')
	pattern4 = re.compile(r'(?<=title=).*(?=_\(basketball\)&action)')
	a = re.search(pattern, url)
	b = re.search(pattern2, url)
	c = re.search(pattern3, url)
	d = re.search(pattern4, url)
	n = ''
	if c:
		n = urllib.unquote(c.group())
	elif d:
		n = urllib.unquote(d.group())
	elif a:
		n = urllib.unquote(a.group())
	elif b:
		n = urllib.unquote(b.group())
	dic['name'] = n.replace("_", " ")
	path = './NBAtemp/' + repr(num)
	f = open(path, 'w')
	total = total + 1
	print dic
	print str(num) + "total" + str(total)
	# out = open(path, 'w')
	# pickle.dump(dic, out)
	# out.close()
	st = ""
	for ic in dic.keys():
		if len(dic[ic]) == 0 or str(ic) == "None" or str(ic) == "":
			continue
		for j in dic[ic]:
			if ic == "name" or ic == "image":
				st = st + j
			else:
				st = st + " " + j
		st = str(ic) + "$" + "\t" + st + "\n"
		f.write(st.encode('utf-8'))
		st = ""
	f.close()
	dic.clear()
	time.sleep(0.5)
