from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    token_facebook = models.CharField(null=True)
    avatar_url = models.URLField(null=True)


    def __unicode__(self):
        return self.name