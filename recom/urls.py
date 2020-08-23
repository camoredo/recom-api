from django.contrib import admin
from django.urls import include, path

api_url_patterns = [
    path('users/', include('users.urls')),
    path('shelves/', include('shelves.urls')),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),
]
