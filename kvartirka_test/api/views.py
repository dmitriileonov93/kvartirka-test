from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Comment, Post

from .serializers import CommentSerializer, PostSerializer


class CreateView(APIView):
    serializer = None

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PostView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(
            post, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentView(APIView):
    def get(self, request, pk):
        comment = Comment.objects.get(id=pk)
        comment_tree = cache_tree_children(
            comment.get_descendants(include_self=True))
        serializer = CommentSerializer(
            comment_tree[0],
            context={'request': request,
                     'depth_level': comment.level})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostCreateView(CreateView):
    serializer = PostSerializer


class CommentCreateView(CreateView):
    serializer = CommentSerializer
