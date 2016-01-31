# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0006_auto_20160131_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetgroup',
            name='neutral',
            field=models.IntegerField(default=0),
        ),
    ]
