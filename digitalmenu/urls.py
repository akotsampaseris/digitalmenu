from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django Apps
    path('admin/', admin.site.urls),
    # Custom Apps
    path('', include('pages.urls')),
    path('user/', include('user.urls')),
]
