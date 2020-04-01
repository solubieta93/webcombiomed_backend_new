from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.decorators import action
from .serializers import UserSerializer, \
    RegisterSerializer, LoginSerializer, RegisterAdminSerializer
from django.contrib.auth.models import User
from knox import views as knox_views
from rest_framework import filters

# TODO: check if we want that any user change username, password or email.Right now only Admin have permissions to do it
# TODO: use active directory to authentication


# Get User API
class Users(ModelViewSet):
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['owner']
    search_fields = ['username']
    ordering_fields = ['id']
    ordering = ['id']

    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    # 'detail': [permissions.IsAuthenticatedOrReadOnly],
                                    # 'retrieve': [permissions.IsAuthenticatedOrReadOnly],
                                    'partial_update': [permissions.IsAdminUser],
                                    'update': [permissions.IsAdminUser],
                                    'destroy': [permissions.IsAdminUser],
                                    'list': [permissions.IsAuthenticatedOrReadOnly]}

    def get_permissions(self):
        try:
            print('try')
            print(self.action)
            a = [permission() for permission in self.permission_classes_by_action[self.action]]
            print(a)
            return a
        except KeyError:
            return [permission() for permission in self.permission_classes]

    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class Auth(GenericViewSet):
    permission_classes_by_action = {'getuser': [permissions.IsAuthenticatedOrReadOnly]}

    def get_permissions(self):
        try:
            print('try')
            print(self.action)
            a = [permission() for permission in self.permission_classes_by_action[self.action]]
            print(a)
            return a
        except KeyError:
            return [permission() for permission in self.permission_classes]

    @action(methods=['post'], detail=False, url_path='login', url_name='login')
    def login(self, request):
        print('estoy en login')
        self.serializer_class = LoginSerializer
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        # if serializer.is_valid():
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        }, status=202)
        # else:
        #     # print(serializer.errors)
        #     # return Response(serializer.errors, status=400)
        #     return Response({
        #         "detail": "Invalid Credentials"
        #     }, status=400)

    @action(methods=['post'], detail=False, url_path='register', url_name='register')
    def register(self, request):
        print(request)
        print(request.data)
        self.serializer_class = RegisterSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

    @action(methods=['post'], detail=False, url_path='register_admin', url_name='register_admin')
    def register_admin(self, request):
        self.serializer_class = RegisterAdminSerializer
        print('estoy en admin')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        }, status=201)

    # Arreglar esto
    @action(methods=['post'], detail=False, url_path='logout', url_name='logout')
    def logout(self, request):
        print(request)
        return knox_views.LogoutView.post(self, request=request)

    @action(methods=['get'], detail=False, url_path='getuser', url_name='getuser')
    def getuser(self, request):
        user = request.user
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data})






