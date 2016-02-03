# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20160122_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='race',
            field=models.ForeignKey(related_name='race', to='races.Race'),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(to='users.UserDetail'),
        ),
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.ForeignKey(default=1, to='states.State', null=True),
        ),
    ]
