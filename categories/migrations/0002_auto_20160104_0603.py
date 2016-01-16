# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 05:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 4, 5, 3, 39, 125145, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 4, 5, 3, 48, 988652, tzinfo=utc)),
            preserve_default=False,
        ),
    ]