from rest_framework import serializers

from drf_extra_fields.geo_fields import PointField
from images.serializers import ImageSerializer
from products.models import Product

class ProductsSerializer(serializers.ModelSerializer):
    location = PointField(required=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'race', 'gender', 'sterile', 'description', 'state', 'price', 'category',
                  'active', 'location', 'created_at')

class ProductsListSerializer(serializers.ModelSerializer):

    race = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()
    gender = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    images = ImageSerializer(many=True)
    location = PointField(required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'race', 'gender', 'seller', 'sterile', 'description', 'state', 'price', 'category',
                  'active', 'location', 'created_at', 'updated_at', 'images')
