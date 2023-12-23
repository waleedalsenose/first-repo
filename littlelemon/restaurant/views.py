from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer,UserSerializer
from django.contrib.auth.models import User, Permission
from rest_framework import viewsets,permissions
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import permission_classes
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class MenuItemView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BookingSerializer
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]
    
def index(request):
    return render(request, 'index.html', {})