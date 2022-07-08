from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .permissions import *
from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_permissions(self):

        if self.action == 'list' or self.action == 'retrieve':
            self.permission_classes = AllowAny,
        else:
            self.permission_classes = IsAuthorPermission,

        return super(PostViewSet, self).get_permissions()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = None
    permission_classes = IsUserPermission | IsAuthorPermission,
