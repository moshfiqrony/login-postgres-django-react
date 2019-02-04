
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('getbyid/', include('login.api.urls')),
    path('getbyuser/', include('login.api.urls2')),
]
