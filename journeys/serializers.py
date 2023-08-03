from rest_framework import serializers
from journeys.models import Journey


class JourneySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source-'owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1548 x 1548 * 2:
            raise serializers.ValidationError(
                "Image size larger than 3MB!"
            )
        if value.image.width > 1920:
            raise serializer.ValidationError(
                "Image with larger than 1920px"
            )
        if value.image.height > 1080:
            raise serializers.ValidationError(
                "Image height larger than 1080px"
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta: 
        model = Journey
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image',
        ]