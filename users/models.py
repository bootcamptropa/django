from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    token_facebook = models.CharField(null=True, max_length=255)
    avatar_url = models.URLField(null=True)