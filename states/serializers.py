# -*- coding: utf-8 -*-

from rest_framework import serializers
from models import State

class StatesSerializer (serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('id', 'name')
