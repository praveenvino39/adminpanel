from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/auth', include('Authorization.urls')),
    path('api/core', include('Order.urls')),
    path('api/generate', include('Report.urls')),
    path('admin/', admin.site.urls),
]
