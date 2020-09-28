from django.shortcuts import render
from myAPP.models import *
# Create your views here.


def showdata(request):
    datalist = basedata.objects.all()
    return render(request, 'index.html', {"data": datalist})