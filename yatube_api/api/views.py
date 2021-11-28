from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post, Follow
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, GroupSerializer,
                          PostSerializer, FollowSerializer)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects


class FollowViewSet(ListCreateAPIView):
    serializer_class = FollowSerializer
    queryset = Follow.objects
