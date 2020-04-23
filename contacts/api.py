from .models import Contact
from .serializers import ContactsSerializer
from rest_framework import viewsets, permissions, filters


class ContactsViewSet(viewsets.ModelViewSet):
    """
    The ModelViewSet automatically provides LIST, CREATE, RETRIEVE, UPDATE and DESTROY actions
    The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(),
    and .destroy().
    """
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['priority']
    ordering = ['priority']
    serializer_class = ContactsSerializer

    permission_classes_by_action = {'create': [permissions.IsAdminUser],
                                    'retrieve': [permissions.IsAdminUser],
                                    'update': [permissions.IsAdminUser],
                                    'destroy': [permissions.IsAdminUser],
                                    'list': [permissions.AllowAny]}

    def get_queryset(self):
        return Contact.objects.all()

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
