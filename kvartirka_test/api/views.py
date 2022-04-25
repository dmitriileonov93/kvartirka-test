from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Comment, Post

from .serializers import CommentSerializer, PostSerializer


class PostCreateView(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentCreateView(APIView):
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class PostView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(
            post,
            context={
                'request': request
            }
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentView(APIView):
    def get(self, request, pk):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(
            comment,
            context={
                'request': request,
                'depth_level': comment.depth_level
            }
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
