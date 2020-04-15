from rest_framework import routers
from .api import ContactsViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('contacts', ContactsViewSet, basename='contacts')

urlpatterns = router.urls
