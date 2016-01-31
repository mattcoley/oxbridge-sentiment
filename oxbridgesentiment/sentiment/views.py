from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TweetGroup
from datetime import datetime, timedelta
from django.utils import timezone
import pandas as pd
import scrape
import json
from django.db.models import Max

def index(request):
    return render(request, 'sentiment/index.html', {})

def update(request,name):
    entry = TweetGroup.objects.filter(name = name).aggregate(Max('date_added'))
    now = timezone.now()
    if entry['date_added__max'] == None or entry['date_added__max'] < (now - timedelta(minutes=5)):
        (pos,neg,neu,m,l) = scrape.likeability(name)
        t = TweetGroup()
        t.name = name
        t.positive = pos
        t.negative = neg
        t.neutral = neu
        t.date_added = now
        t.best_text = m
        t.worst_text = l
        t.save()
    t = TweetGroup.objects.filter(name = name).order_by('-date_added')[0]
    return HttpResponse(json.dumps({'name':t.name,'positive':t.positive,'negative':t.negative,'neutral':t.neutral,'best-text':t.best_text,'worst-text':t.worst_text}))

