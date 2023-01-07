from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    metadata = serializers.JSONField(
                    write_only=True
                )

    class Meta:
        model = Photo
        fields = '__all__'
