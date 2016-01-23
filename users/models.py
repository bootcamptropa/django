from django.db import models
from django.contrib.auth.models import User


class UserDetail(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    token_facebook = models.CharField(null=True, max_length=255)
    avatar_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _get_avatar_thumbnail_url(self):
        return "https://s3.amazonaws.com/walladog/thumbnails/" + self.user.username + ".png"
    avatar_thumbnail_url = property(_get_avatar_thumbnail_url)

    def _get_products_count(self):
        from products.models import Product
        return Product.objects.filter(seller=self.user.id).filter(active=1).count()
    products_count = property(_get_products_count)

    def __unicode__(self):
        if self.user.first_name or self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        else:
            return self.user.username

    def __str__(self):
        if self.user.first_name or self.user.last_name:
            return self.user.first_name + " " + self.user.last_name
        else:
            return self.user.username

