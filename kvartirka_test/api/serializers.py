from django.conf import settings
from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework import serializers

from posts.models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, comment):
        max_depth = settings.MAX_DEPTH
        comment_level = int(self.context.get('depth_level', 0))
        max_depth += comment_level
        if comment.get_level() >= max_depth:
            return []
        children = comment.get_children()
        return CommentSerializer(
            children, many=True, context=self.context).data

    class Meta:
        model = Comment
        fields = ('id', 'text', 'post', 'parent', 'children')


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, post):
        comments = cache_tree_children(
            Comment.objects.filter(
                post=post, level__lte=settings.MAX_DEPTH - 1))
        serializer = CommentSerializer(
            comments,
            many=True,
            context=self.context)
        return serializer.data

    class Meta:
        model = Post
        fields = ('id', 'text', 'comments')
