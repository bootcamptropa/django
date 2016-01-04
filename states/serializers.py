from rest_framework import serializers
from states.models import State

class StatesSerializer (serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('id', 'name')
