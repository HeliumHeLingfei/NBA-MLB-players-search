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

num = 0
inp = open('NBAplayerslist', 'r')
players = pickle.load(inp)
inp.close()

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
		image = infobox[0].find(class_='image').img['src']
		imurl='https:'+image
		print imurl

		tp = re.search(r'\.\w+$', imurl).start()-len(imurl)
		tail = imurl[tp:]
		print tail
		urllib.urlretrieve(imurl, './pic/' + repr(num) + tail)