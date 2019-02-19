from .userDetailsView import UserDetailsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserDetailsView, basename='userinfo')
urlpatterns = router.urls
