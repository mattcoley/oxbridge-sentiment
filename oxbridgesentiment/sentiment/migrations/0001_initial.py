# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.DecimalField(decimal_places=5, max_digits=5)),
                ('url', models.URLField()),
                ('num_retweets', models.IntegerField()),
                ('school', models.CharField(max_length=10)),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]
