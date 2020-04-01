from blog.models import Post, Comment
from rest_framework import viewsets, permissions, decorators
from .serializers import BlogSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django_filters


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    # DjangoFilterBackend,
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['owner']
    search_fields = ['title', 'owner__username', 'publish']
    ordering_fields = ['publish']
    ordering = ['publish']
    is_news = django_filters.BooleanFilter(field_name='news', method='filter_is_news')

    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    # 'detail': [permissions.IsAuthenticatedOrReadOnly],
                                    'retrieve': [permissions.IsAuthenticatedOrReadOnly],
                                    'update': [permissions.IsAdminUser],
                                    'destroy': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticatedOrReadOnly],
                                    'delete': [permissions.IsAdminUser]}

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        try:
            print('try')
            print(self.action)
            a = [permission() for permission in self.permission_classes_by_action[self.action]]
            print(a)
            return a
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def filter_is_news(self):
        pass


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_permissions(self):
        permissions_classes = [
            permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly
        ]
        return [permission() for permission in permissions_classes]

    # This only return if the user is authenticated
    # def get_queryset(self):
    #     return self.request.user.products.all()

    def get_queryset(self):
        # try:
        #     return Comment.objects.filter(owner=self.request.user)
        # except:
            return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
