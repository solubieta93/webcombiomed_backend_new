from rest_framework import routers
from .api import ProductViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('api/products', ProductViewSet, basename='products')
# router.register('api/products/<int:pk>/', ProductViewSet, basename='products')

urlpatterns = router.urls
