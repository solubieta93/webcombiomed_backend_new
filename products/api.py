from .models import Product, ProductType
from rest_framework import viewsets, permissions, filters
from .serializers import ProductSerializer, ProductTypeSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    """
    The ModelViewSet automatically provides LIST, CREATE, RETRIEVE, UPDATE and DESTROY actions
    The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(),
    and .destroy().
    """
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['typeId']
    search_fields = ['name']
    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    # 'detail': [permissions.IsAuthenticatedOrReadOnly],
                                    'retrieve': [permissions.IsAuthenticatedOrReadOnly],
                                    'update': [permissions.IsAdminUser],
                                    'destroy': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticatedOrReadOnly]}

    def get_queryset(self):
        print(self.request.user.is_superuser)
        print('estoy en query set')
        # if self.request.method in permissions.SAFE_METHODS:
        return Product.objects.all()

        # # To see only products below user
        # return Product.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        print('estoy en el create')
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    The ModelViewSet automatically provides LIST, CREATE, RETRIEVE, UPDATE and DESTROY actions
    The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(),
    and .destroy().
    """
    serializer_class = ProductTypeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'retrieve': [permissions.IsAdminUser],
                                    'update': [permissions.IsAdminUser],
                                    'destroy': [permissions.IsAdminUser],
                                    'list': [permissions.AllowAny]}

    def get_queryset(self):
        return ProductType.objects.all()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
