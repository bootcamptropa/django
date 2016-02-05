# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20160201_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='race',
            field=models.ForeignKey(related_name='race', to='races.Race', null=True),
        ),
    ]
