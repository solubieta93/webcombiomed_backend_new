from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from products.models import Product
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action,permission_classes


# ViewSets define the view behavior.
# The viewset classes are almost the same things as view class, except they are provide operations as READ or UPDATE
# but not methods handlers such as GET or PUT
# ModelViewSet hereda de GenericAPIView
class ProductViewSet(viewsets.ModelViewSet):
    """
    The ModelViewSet automatically provides LIST, CREATE, RETRIEVE, UPDATE and DESTROY actions
    The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(),
    and .destroy().
    """
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_permissions(self):
    #     permissions_classes = [
    #         permissions.IsAuthenticatedOrReadOnly,
    #         # permissions.IsAdminUser,
    #     ]
    #     return [permission() for permission in permissions_classes]

    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    # 'detail': [permissions.IsAuthenticatedOrReadOnly],
                                    'retrieve': [permissions.IsAuthenticatedOrReadOnly],
                                    'update': [permissions.IsAdminUser],
                                    'destroy': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticatedOrReadOnly]}

    # This only return if the user is authenticated
    # def get_queryset(self):
    #     return self.request.user.products.all()

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
            print('try')
            print(self.action)
            a = [permission() for permission in self.permission_classes_by_action[self.action]]
            print(a)
            return a
        except KeyError:
            return [permission() for permission in self.permission_classes]
