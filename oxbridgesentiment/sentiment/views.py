from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TweetGroup
from datetime import datetime, timedelta
from django.utils import timezone
import pandas as pd
import scrape

def index(request):
    return render(request, 'sentiment/index.html', {})

def update(request,name):

    from django.db.models import Max

    entry = TweetGroup.objects.filter(name = name).aggregate(Max('date_added'))
    now = timezone.now()
    if entry['date_added__max'] == None or entry['date_added__max'] < (now - timedelta(minutes=5)):
        (pos,neg) = scrape.likeability(name)
        t = TweetGroup()
        t.name = name
        t.positive = pos
        t.negative = neg
        t.date_added = now
        t.save()
        print (pos,neg)


