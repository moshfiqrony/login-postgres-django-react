from .view import UserInfoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserInfoView, basename='userinfo')
urlpatterns = router.urls
