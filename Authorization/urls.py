from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet

router = DefaultRouter()
router.register('/user', UserViewSet)

urlpatterns = [
    path('/login/', obtain_auth_token),
    path('', include(router.urls)),
]
