from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.


class UserViewSet(ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.POST.get('password')))
    serializer_class = UserSerializer
    authentication_class = TokenAuthentication
    permission_classes =[IsAuthenticated]
    queryset = User.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        elif self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super(UserViewSet, self).get_permissions()
