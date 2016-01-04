
from rest_framework import serializers
from products.models import Product


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        # read_only_fields = ('category', 'state', 'races', 'seller')

# class ProductsListSerializer(serializers.ModelSerializer):
#
#     category = serializers.StringRelatedField()
#     state = serializers.StringRelatedField()
#     seller = serializers.StringRelatedField()
#
#     class Meta(ProductsSerializer.Meta):
#         fields = ('id', 'name', 'price', 'description', 'category', 'state', 'seller', 'images')





    # def create(self, validated_data):
    #     instance = Product()
    #     product_data = validated_data.get('product')
    #     product = Product.objects.create_user(username=product_data.get('username'),
    #                                           email=product_data.get('email'),
    #                                           password=product_data.get('password'),
    #                                           first_name=product_data.get('first_name'),
    #                                           last_name=product_data.get('last_name'))
    #     if product:
    #         instance.product = product
    #         product_ext = self.update(instance, validated_data)
    #
    #     return product_ext