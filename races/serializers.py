# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Race

class RacesSerializer (serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = ('id', 'name')