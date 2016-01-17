from django.db import models
from users.models import UserDetail
from races.models import Race
from states.models import State
from categories.models import Category
from products.settings import GENDERS

class Product(models.Model):
    name = models.CharField(max_length=30)
    race = models.ForeignKey(Race, null=False)
    seller = models.ForeignKey(UserDetail, null=False)
    gender = models.CharField(max_length=3, choices=GENDERS, default='NON')
    sterile = models.BooleanField(default=False)
    description = models.CharField(max_length=250, default='')
    state = models.ForeignKey(State)
    price = models.FloatField(null=False, default=0)
    category = models.ForeignKey(Category)
    active = models.BooleanField(null=False, default=True)
    longitude = models.FloatField(null=False)
    latitude = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
