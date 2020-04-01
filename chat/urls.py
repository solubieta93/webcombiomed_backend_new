from .api import ChatSessionMessageViewSet, ChatSessionViewSet
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
router.register('chat', ChatSessionViewSet, base_name='chat')
# router.register('api/chat/<uri>', ChatSessionViewSet, basename='chat_uri')
router.register('chat/messages', ChatSessionMessageViewSet, basename='chat_messages')


urlpatterns = router.urls
