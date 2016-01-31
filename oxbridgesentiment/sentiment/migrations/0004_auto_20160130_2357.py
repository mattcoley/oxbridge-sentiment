# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0003_auto_20160130_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetgroup',
            name='negative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tweetgroup',
            name='positive',
            field=models.IntegerField(default=0),
        ),
    ]
