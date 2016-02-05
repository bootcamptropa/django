from rest_framework import serializers

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'name', 'photo_url', 'photo_thumbnail_url')
