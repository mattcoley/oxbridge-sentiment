# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0007_tweetgroup_neutral'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetgroup',
            name='total_score',
            field=models.DecimalField(default=0.0, max_digits=5, decimal_places=5),
        ),
    ]
