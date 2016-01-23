from rest_framework import serializers

from images.serializers import ImageSerializer
from products.models import Product
from users.serializers import UserPublicListSerializer


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'race', 'gender', 'sterile', 'description', 'state', 'price', 'category',
                  'active', 'created_at')

class ProductsListSerializer(serializers.ModelSerializer):

    race = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    images = ImageSerializer(many=True)
    seller = UserPublicListSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'race', 'gender', 'seller', 'sterile', 'description', 'state', 'price', 'category',
                  'active', 'latitude', 'longitude', 'created_at', 'updated_at', 'images', 'raceid', 'genderid', 'stateid', 'categoryid')
