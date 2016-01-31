# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0005_auto_20160131_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetgroup',
            name='best_text',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='tweetgroup',
            name='worst_text',
            field=models.CharField(default='', max_length=500),
        ),
    ]
