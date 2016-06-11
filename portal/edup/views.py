from django.shortcuts import render

from django.http import HttpResponse
from edup.models import school

from ajax_search.forms import SearchForm

def index(request):
	a=[]
	res = school.objects.all()
	for i in res:
		a.append(i)
	print a
	return render(request,'index.html',{'cat':a})


