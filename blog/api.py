from blog.models import Post, Comment
from rest_framework import viewsets, permissions, decorators
from .serializers import BlogSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django_filters
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend


# TODO: filter by news, boolean filter
class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    # DjangoFilterBackend,
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['news', 'owner', 'publish']
    search_fields = ['title', 'owner__username']
    ordering_fields = ['publish']
    ordering = ['-publish']
    # is_news = django_filters.BooleanFilter(field_name='news', method='filter_is_news')

    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    # 'detail': [permissions.IsAuthenticatedOrReadOnly],
                                    'retrieve': [permissions.IsAuthenticatedOrReadOnly],
                                    'update': [permissions.IsAdminUser],
                                    'destroy': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticatedOrReadOnly],
                                    'delete': [permissions.IsAdminUser]}

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

    def get_queryset(self):
        return Post.objects.all()

    @action(methods=['get'], detail=False, url_path='blog', url_name='blog')
    def getblog(self, request):
        print(request.query_params)
        offset = int(request.query_params['offset']) if 'offset' in request.query_params else 0
        limit = int(request.query_params['limit']) if 'limit' in request.query_params else 10
        id_distinct = int(request.query_params['id_distinct']) if 'id_distinct' in request.query_params else -1
        if id_distinct != -1:
            queryset = Post.objects.all().filter(~Q(id=id_distinct)).order_by('-updated')
        else:
            queryset = Post.objects.all().order_by('-updated')
        end = offset + limit
        count = queryset.count()

        if offset >= count:
            return Response({
                'success': False,
                'message': 'Bad query params.',
                'data': None,
            }, status=400)
        posts = [BlogSerializer(post, context=self.get_serializer_context()).data for post in queryset[offset: end]]
        return Response({
            'success': True,
            'message': 'Success',
            'data': {
                'count': count,
                'hasMore': count >= end + 1,
                'results': posts,
            },
        }, status=200)

    @action(methods=['get'], detail=False, url_path='news', url_name='news')
    def getnews(self, request):
        queryset = Post.objects.filter(news=True)
        offset = int(request.query_params['offset']) if 'offset' in request.query_params else 0
        limit = int(request.query_params['limit']) if 'limit' in request.query_params else 10
        start = offset * limit
        end = start + limit
        count = queryset.count()

        if start >= count:
            return Response({
                'success': False,
                'message': 'Bad query params.',
                'data': None,
            }, status=400)
        news = [BlogSerializer(post, context=self.get_serializer_context()).data for post in queryset[start: end]]
        return Response({
            'success': True,
            'message': 'Success',
            'data': {
                'count': count,
                'hasMore': count > (offset + 1) * limit,
                'news': news,
            },
        }, status=200)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_permissions(self):
        permissions_classes = [
            permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly
        ]
        return [permission() for permission in permissions_classes]

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
