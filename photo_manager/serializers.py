from rest_framework import serializers

from .models import Photo


class PhotoListSerializer(serializers.ModelSerializer):
    metadata = serializers.JSONField(
                    write_only=True
                )

    class Meta:
        model = Photo
        fields = '__all__'


class PhotoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
