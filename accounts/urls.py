from .api import Users, Auth
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'auth', Auth, basename='auth')
router.register(r'users', Users, basename='user')
urlpatterns = router.urls

