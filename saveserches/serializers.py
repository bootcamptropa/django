from rest_framework import serializers
from saveserches.models import SavedSearch

class SaveSerchesSerializer (serializers.ModelSerializer):

    class Meta:
        model = SavedSearch

class SaveSerchesListSerializer (serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    race = serializers.StringRelatedField()

    class Meta:
        model = SavedSearch
        fields = ('keywords', 'category', 'latitude', 'longitude', 'race')