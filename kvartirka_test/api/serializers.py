from django.conf import settings
from rest_framework import serializers

from posts.models import Comment, Post


class FilterCommentRecursiveListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        max_depth = settings.MAX_DEPTH
        depth_level = self.context.get('depth_level', 0)
        max_depth += int(depth_level)
        data = data.filter(depth_level__lte=max_depth)
        return super().to_representation(data)


class FilterCommentListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveCommentSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

    class Meta:
        list_serializer_class = FilterCommentRecursiveListSerializer


class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'text', 'parent', 'children')
        list_serializer_class = FilterCommentListSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'comments')
