"""ViewsSet for the chat app."""

from django.http import Http404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, serializers
from rest_framework.response import Response
from .models import (
    ChatSession, ChatSessionMember, ChatSessionMessage, deserialize_user
)
from .serializers import ChatSessionSerializer, ChatSessionMessageSerializer
from rest_framework.decorators import action
# from notifications.signals import notify


class ChatSessionViewSet(viewsets.ModelViewSet):
    """Manage Chat sessions."""
    serializer_class = ChatSessionSerializer

    def get_permissions(self):
        permissions_classes = [
            permissions.IsAuthenticated,
        ]
        return [permission() for permission in permissions_classes]

    def get_queryset(self):
        # if self.request.method in permissions.SAFE_METHODS:
        return ChatSession.objects.all()

    # def post(self, serializer):
    #     serializer.save(owner=self.request.user)
    #     return Response({
    #         'status': 'SUCCESS', 'uri': serializer.uri,
    #         'message': 'New chat session created'
    #     })

    # def post(self, request, *args, **kwargs):
    #     """create a new chat session."""
    #     user = request.user
    #     chat_session = ChatSession(owner_id=user.id)
    #     chat_session.save()
    #
    #     return Response({
    #         'status': 'SUCCESS', 'uri': chat_session.uri,
    #         'message': 'New chat session created'
    #     })

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])#, url_path='patch', url_name='patch')
    def patch(self, request, pk=None):
        """Add a user to a chat session."""
        User = get_user_model()

        uri = pk
        print(uri)
        username = request.data['username']
        user = User.objects.get(username=username)

        chat_session = ChatSession.objects.get(uri=uri)
        owner = chat_session.owner

        if owner != user:  # Only allow non owners join the room
            chat_session.members.get_or_create(
                user=user, chat_session=chat_session
            )

        owner = deserialize_user(owner)
        members = [
            deserialize_user(chat_session.user)
            for chat_session in chat_session.members.all()
        ]
        members.insert(0, owner)  # Make the owner the first member

        return Response({
            'status': 'SUCCESS', 'members': members,
            'message': '%s joined that chat' % user.username,
            'user': deserialize_user(user)
        })


class ChatSessionMessageViewSet(viewsets.ModelViewSet):
    """Create/Get Chat session messages."""
    serializer_class = ChatSessionMessageSerializer

    def get_permissions(self):
        permissions_classes = [
            permissions.IsAuthenticated,
        ]
        return [permission() for permission in permissions_classes]

    @action(detail=True,  methods=['get'])
    def get_message(self, request, pk=None):
        print('entro al get')
        """return all messages in a chat session."""
        uri = pk

        chat_session = ChatSession.objects.get(uri=uri)
        messages = [chat_session_message.to_json()
                    for chat_session_message in chat_session.messages.all()]

        return Response({
            'id': chat_session.id, 'uri': chat_session.uri,
            'messages': messages
        })

    @action(detail=True, methods=['post'])
    def send_message(self, request, pk=None):
        """create a new message in a chat session."""
        print('entro')
        uri = pk
        message = request.data['message']

        user = request.user
        chat_session = ChatSession.objects.get(uri=uri)

        chat_session_message = ChatSessionMessage.objects.create(
            user=user, chat_session=chat_session, message=message
        )

        notif_args = {
            'source': user,
            'source_display_name': user.get_full_name(),
            'category': 'chat', 'action': 'Sent',
            'obj': chat_session_message.id,
            'short_description': 'You a new message', 'silent': True,
            'extra_data': {
                'uri': chat_session.uri,
                'message': chat_session_message.to_json()
            }
        }
        # notify.send(
        #     sender=self.__class__, **notif_args, channels=['websocket']
        # )

        return Response({
            'status': 'SUCCESS', 'uri': chat_session.uri, 'message': message,
            'user': deserialize_user(user)
        })


def raise_404(request):
    """Raise a 404 Error."""
    raise Http404