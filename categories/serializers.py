# -*- coding: utf-8 -*-
from rest_framework import serializers

class CategorySerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    active = serializers.BooleanField()