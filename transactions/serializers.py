from rest_framework import serializers
from transactions.models import Transaction


class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'product')

class TransactionsListSerializer(serializers.ModelSerializer):

    seller = serializers.StringRelatedField()
    product = serializers.StringRelatedField()
    buyer = serializers.StringRelatedField()

    class Meta:
        model = Transaction
