from rest_framework import serializers
from .models import Blog
from likes_blogs.models import LikeBlog


class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()


    def validate_image(self, value):
        if value.size > 2 * 1528 * 1528:
            raise serializers.ValidationError(
                'Image size larger than 3MB!'
            )
        if value.image.width > 1920:
            raise serializers.ValidationError(
                'Image width larger than 1920px!'
            )
        if value.image.height > 1080:
            raise serializers.ValidationError(
                'Image height larger than 1080px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            likeblog = LikeBlog.objects.filter(
                owner=user, blog=obj
            ).first()
            return likeblog.id if likeblog else None
        return None

    class Meta:
        model = Blog
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'countries', 'locations', 
            'image', 'like_id', 'likes_count',
        ]