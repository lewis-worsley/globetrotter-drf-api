from django.db import IntegrityError
from rest_framework import serializers
from .models import LikeBlog


class LikeBlogSerializer(serializers.ModelSerializer):
    """
    Serializer for the LikeBlog model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LikeBlog
        fields = [
            'id', 'created_at', 'owner', 'blog',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
