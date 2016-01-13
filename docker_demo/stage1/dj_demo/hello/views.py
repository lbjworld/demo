from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now {now}.</body></html>".format(now=now)
    return HttpResponse(html)

