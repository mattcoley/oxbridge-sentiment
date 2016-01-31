from __future__ import unicode_literals

from django.db import models


class TweetGroup(models.Model):
    sentiment = models.DecimalField(max_digits=5, decimal_places=5,default = 0.0)
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField()
    positive = models.IntegerField(default = 0)
    negative = models.IntegerField(default = 0)
    neutral = models.IntegerField(default=0)
    best_text = models.CharField(max_length=500,default="")
    worst_text = models.CharField(max_length = 500,default="")
    total_score = models.DecimalField(max_digits=25,decimal_places=5,default= 0.0)
