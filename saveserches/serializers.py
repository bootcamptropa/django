from rest_framework import serializers
from saveserches.models import SavedSearch

class SaveSearchesSerializer (serializers.ModelSerializer):

    class Meta:
        model = SavedSearch

class SaveSearchesListSerializer (serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    race = serializers.StringRelatedField()

    class Meta:
        model = SavedSearch
        fields = ('id', 'name', 'keywords', 'category', 'latitude', 'longitude', 'race')