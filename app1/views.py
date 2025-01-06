from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def server_time(request):
    date=datetime.datetime.now()
    msg='<p> Server time is :'+str(date)+'</p>'
    return HttpResponse(msg)

    