import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F
from django.conf import settings 

from models import Counter

def hello(request):
    now = datetime.datetime.now()
    # update counter 
    Counter.objects.filter(name=settings.STAT_NAME).update(count=F('count')+1)
    c = Counter.objects.get(name=settings.STAT_NAME)
    html = "<html><body>\
                It is now {now}, count : {c}. <br/>\
            </body></html>".format(now=now, c=c.count)
    return HttpResponse(html)

