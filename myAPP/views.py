from django.shortcuts import render
from myAPP.models import *
# Create your views here.


def showdata(request):
    datalist = basedata.objects.all()
    return render(request, 'index.html', {"data": datalist})

def originaldata(request):
    datalist = basedata.objects.all()
    return render(request, 'original_data_tab.html', {"data": datalist})

def data_description(request):
    return render(request, '折线图.html')
