from rest_framework import routers
from .api import ProductViewSet, ProductTypeViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('api/products', ProductViewSet, basename='products')
router.register('api/types/products', ProductTypeViewSet, basename='productsType')

urlpatterns = router.urls
