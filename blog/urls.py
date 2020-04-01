from rest_framework import routers
from .api import BlogViewSet, CommentViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('blog', BlogViewSet, basename='blog')
router.register(r'comment', CommentViewSet, basename='comment')


urlpatterns = router.urls
