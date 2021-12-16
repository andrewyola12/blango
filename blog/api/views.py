from rest_framework import generics
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject
from blango_auth.models import User
from blog.api.serializers import PostSerializer, UserSerializer
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AuthorModifyOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    
class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer