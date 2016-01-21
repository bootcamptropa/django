from rest_framework import serializers

from images.serializers import ImageSerializer
from products.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'race', 'seller', 'gender', 'sterile', 'description', 'state', 'price', 'category',
                  'active', 'longitude', 'latitude', 'created_at', 'images')