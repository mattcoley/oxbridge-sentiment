# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0008_tweetgroup_total_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetgroup',
            name='total_score',
            field=models.DecimalField(default=0.0, max_digits=25, decimal_places=5),
        ),
    ]
