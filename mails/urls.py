from rest_framework import routers
from .api import MailViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'mail', MailViewSet, basename='mail')
urlpatterns = router.urls
