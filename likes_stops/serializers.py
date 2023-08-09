from django.db import IntegrityError
from rest_framework import serializers
from .models import LikeStop


class LikeStopSerializer(serializers.ModelSerializer):
    """
    Serializer for the LikeStop model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LikeStop
        fields = [
            'id', 'created_at', 'owner', 'journey', 'stop'
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })