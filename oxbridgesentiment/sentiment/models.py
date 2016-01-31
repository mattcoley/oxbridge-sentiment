from __future__ import unicode_literals

from django.db import models


class TweetGroup(models.Model):
    sentiment = models.DecimalField(max_digits=5, decimal_places=5)
    name = models.CharField(max_length=30)
    date_added = models.DateTimeField()
    positive = models.IntegerField(default = 0)
    negative = models.IntegerField(default = 0)
