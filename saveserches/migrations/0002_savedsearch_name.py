# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('saveserches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedsearch',
            name='name',
            field=models.CharField(default=b'FAVORITO', max_length=60),
            preserve_default=False,
        ),
    ]
