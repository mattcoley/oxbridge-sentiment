# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0004_auto_20160130_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetgroup',
            name='sentiment',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=5),
        ),
    ]
