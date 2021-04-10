from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)
from .permissions import (
    AuthorAccessPermission,
    IsSuperUserOrStaffOrPermission
)
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from accounts.models import User
from post.models import Post


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorAccessPermission, IsAuthenticated)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsSuperUserOrStaffOrPermission,)

    def get_queryset(self):
        user = User.objects.get(pk=self.request.user.pk)