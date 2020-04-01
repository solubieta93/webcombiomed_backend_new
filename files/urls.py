from rest_framework import routers

from files.views import FilesView

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'files', FilesView, basename='files')
# router.register(r'users', Users, basename='user')
urlpatterns = router.urls
