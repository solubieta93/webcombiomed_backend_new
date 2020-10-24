from rest_framework import serializers
from .models import Post, Comment


class BlogSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    details_es = serializers.ReadOnlyField(source='load_details_es', default=None, )
    details_en = serializers.ReadOnlyField(source='load_details_en', default=None, )
    files = serializers.ReadOnlyField(source='load_files', default=None, )
    title_json = serializers.ReadOnlyField(source='load_title', default=None)
    abstract_json = serializers.ReadOnlyField(source='load_abstract', default=None)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'
