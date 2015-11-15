from django.db import models
from django.contrib.auth.models import User
from races.models import Race
from states.models import State
from categories.models import Category
from products.settings import GENDERS

class Product(models.Model):
    name = models.CharField(max_length=30)
    race = models.ForeignKey(Race)
    seller = models.ForeignKey(User)
    gender = models.CharField(max_length=3, choices=GENDERS, default='NON')
    sterile = models.BooleanField(default=False)
    description = models.CharField(max_length=250, default='')
    published_date = models.DateTimeField(auto_now_add=True)
    state = models.ForeignKey(State)
    price = models.FloatField(default=0)
    category = models.ForeignKey(Category)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name