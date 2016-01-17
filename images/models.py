from django.db import models
from products.models import Product

class Image(models.Model):
    name = models.CharField(max_length=30)
    photo_url = models.URLField()
    photo_thumbnail_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __unicode__(self):
        return self.name
