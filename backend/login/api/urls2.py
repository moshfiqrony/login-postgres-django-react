from .viewByUID import UserInfoViewById
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserInfoViewById, basename='userinfo')
urlpatterns = router.urls