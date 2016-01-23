from django.contrib.gis.db import models
from users.models import UserDetail
from races.models import Race
from states.models import State
from categories.models import Category
from products.settings import GENDERS

class Product(models.Model):
    name = models.CharField(max_length=30)
    race = models.ForeignKey(Race, null=False, related_name='race')
    seller = models.ForeignKey(UserDetail, null=False)
    gender = models.CharField(max_length=3, choices=GENDERS, default='NON')
    sterile = models.BooleanField(default=False)
    description = models.CharField(max_length=250, default='')
    state = models.ForeignKey(State)
    price = models.FloatField(null=False, default=0)
    category = models.ForeignKey(Category)
    active = models.BooleanField(null=False, default=True)
    location = models.PointField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _get_latitude(self):
        return str(self.location.x)
    latitude = property(_get_latitude)

    def _get_longitude(self):
        return str(self.location.y)
    longitude = property(_get_longitude)

    def _get_race_id(self):
        return str(0)
    raceid = property(_get_race_id)

    def _get_gender_id(self):
        return str(0)
    genderid = property(_get_gender_id)

    def _get_state_id(self):
        return str(0)
    stateid = property(_get_state_id)

    def _get_category_id(self):
        return str(0)
    categoryid = property(_get_category_id)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
