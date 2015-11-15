from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Transaction(models.Model):
    product = models.ForeignKey(Product)
    seller = models.ForeignKey(User, related_name='user_seller')
    buyer = models.ForeignKey(User, related_name='user_buyer')
    date_transaction = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.product