from django.urls import path

from .views import CommentCreateView, CommentView, PostCreateView, PostView

urlpatterns = [
    path('post/', PostCreateView.as_view()),
    path('comment/', CommentCreateView.as_view()),
    path('post/<int:pk>/', PostView.as_view()),
    path('comment/<int:pk>/', CommentView.as_view()),
]
