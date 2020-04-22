from rest_framework import serializers
from .models import Post, Comment


class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    details = serializers.ReadOnlyField(source='load_details', default=None, )
    files = serializers.ReadOnlyField(source='load_files', default=None, )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'
