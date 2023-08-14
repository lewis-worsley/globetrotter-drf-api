from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from comments_stops.models import CommentStop


class CommentStopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = CommentStop
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'stop', 'created_at', 'updated_at', 'content',
        ]


class CommentStopDetailSerializer(CommentStopSerializer):
    """
    Serializer for the CommentStop model used in detail view
    Stop is a read only field so that we don't have to set it on each update
    """
    stop = serializers.ReadOnlyField(source='stop.id')