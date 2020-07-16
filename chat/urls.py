from .api import ChatSessionMessageViewSet, ChatSessionViewSet
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter()
router.register('chat', ChatSessionViewSet, basename='chat')
# router.register('api/chat/<uri>', ChatSessionViewSet, basename='chat_uri')
router.register('chat/messages', ChatSessionMessageViewSet, basename='chat_messages')


urlpatterns = router.urls
