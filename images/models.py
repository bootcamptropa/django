from django.db import models
from products.models import Product

class Image(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey(Product)
    photo_url = models.URLField()

    def __unicode__(self):
        return self.name