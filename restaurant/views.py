from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from restaurant.models import Booking, Menu
from restaurant.serializers import UserSerializer, BookingSerializer, MenuSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# def index(request):
#     return render(request, 'index.html', {})


# The permission_classes attributein the ViewSet class is set to the IsAuthenticated class. This makes the unauthentictated user unable to access this view.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemViewSet(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer