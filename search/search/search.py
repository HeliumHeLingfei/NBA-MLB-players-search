# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
import cPickle as pickle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings


@csrf_exempt
def search(request):
	settings.RE = []
	inp = open('D:/Program Files (x86)/python2.7/search/static/dic', 'rb')
	settings.DIC = pickle.load(inp)
	inp.close()
	inp = open('D:/Program Files (x86)/python2.7/search/static/playerlist', 'rb')
	settings.PLI = pickle.load(inp)
	inp.close()
	return render(request, "search.html")


def result(request):
	if 'name' in request.GET:
		getre(request)
		if len(settings.RE) == 0:
			return render(request, "search.html")
	resultlist = settings.RE
	paginator = Paginator(resultlist, 5)  # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	# searchlist = [{'属性1': 1, '属性2': 3}, {'pro1': 'df', "pro2": 'df'}]
	return render(request, "result.html", {'contacts': contacts})


def getre(request):
	searchresult = {}
	resultlist = []
	for i in request.GET:
		print i
		print request.GET[i]
		if request.GET[i] == i:
			continue
		searchresult[i] = request.GET[i].lower().split()
	print searchresult
	if len(searchresult) == 0:
		return search(request)
	dic=settings.DIC
	playerlist=settings.PLI
	res = set()
	nu = 0
	print dic.keys()
	for i in searchresult:
		print searchresult[i]
		if nu == 0:
			nu = nu + 1
			if len(searchresult[i]) ==1:
				res = dic[i][searchresult[i][0]]
			else:
				res= dic[i][searchresult[i][0]]
				for q in searchresult[i]:
					print q
					res=res& dic[i][q]
			continue
		if len(searchresult[i]) == 1:
			res = res&dic[i][searchresult[i][0]]
		else:
			for q in searchresult[i]:
				print q
				res = res & dic[i][q]
	for j in res:
		resultlist.append(playerlist[int(j)])
	settings.RE = resultlist
