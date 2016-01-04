from rest_framework import serializers
from races.models import Race

class RacesSerializer (serializers.ModelSerializer):

    class Meta:
        model = Race
        fields = ('id', 'name')