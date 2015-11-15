# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('states', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(default=b'NON', max_length=3, choices=[(b'MAL', b'Male'), (b'FEM', b'Female'), (b'NON', b'')])),
                ('sterile', models.BooleanField(default=False)),
                ('description', models.CharField(default=b'', max_length=250)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='categories.Category')),
                ('race', models.ForeignKey(to='races.Race')),
                ('seller', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('state', models.ForeignKey(to='states.State')),
            ],
        ),
    ]
