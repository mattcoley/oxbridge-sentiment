# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentiment', '0002_auto_20160130_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweetgroup',
            old_name='word',
            new_name='name',
        ),
    ]
