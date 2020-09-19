from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class OrderViewset(ModelViewSet):
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
