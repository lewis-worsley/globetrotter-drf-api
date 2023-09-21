from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):

    def validate_image(self, value):
        if value.size > 2 * 2000 * 2000:
            raise serializers.ValidationError(
                'Image size larger than 4MB!'
            )
        if value.image.width > 1920:
            raise serializers.ValidationError(
                'Image width larger than 1920px!'
            )
        if value.image.height > 1920:
            raise serializers.ValidationError(
                'Image height larger than 1920px!'
            )
        return value

    class Meta:
        model = News
        fields = [
            'id', 'title', 'content', 'created_at', 'updated_at',
            'image',
        ]
