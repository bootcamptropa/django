
from rest_framework import serializers
from products.models import Product


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        read_only_fields = ('category', 'state', 'races', 'seller')

class ProductsListSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    class Meta(ProductsSerializer.Meta):
        fields = ('id', 'name', 'price', 'description', 'category', 'state', 'seller', 'images')