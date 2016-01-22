from rest_framework import serializers

from images.serializers import ImageSerializer
from products.models import Product

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'race', 'gender', 'sterile', 'description', 'state', 'price', 'category',
                  'active', 'location', 'created_at')

class ProductsListSerializer(serializers.ModelSerializer):

    race = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'race', 'gender', 'seller', 'sterile', 'description', 'state', 'price', 'category',
                  'active', 'latitude', 'longitude', 'created_at', 'updated_at', 'images')
