from __future__ import unicode_literals

from django.db import models


class Tweet(models.Model):
    sentiment = models.DecimalField(max_digits=5, decimal_places=5)
    url = models.URLField()
    num_retweets = models.IntegerField()
    school = models.CharField(max_length=10)
    date_added = models.DateTimeField()
