# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_transaction', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(related_name='user_buyer', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(to='products.Product')),
                ('seller', models.ForeignKey(related_name='user_seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
