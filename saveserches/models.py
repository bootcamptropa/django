from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from races.models import Race

class SavedSearch(models.Model):
    user = models.ForeignKey(User)
    keywords = models.CharField(max_length=80)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    category = models.ForeignKey(Category)
    race = models.ForeignKey(Race)

    def __unicode__(self):
        return self.keywords
