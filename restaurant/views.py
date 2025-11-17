from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from restaurant.models import Booking, Menu
from restaurant.serializers import UserSerializer, BookingSerializer, MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# def index(request):
#     return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MenuItemViewSet(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class SingleMenuItemViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]