from django.shortcuts import render
from rest_framework import viewsets

from .models import Customer, Seller
from .serializers import CustomerSerialazer, SellerSerialazer

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerialazer
    queryset = Customer.objects.all()

class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerialazer
    queryset = Seller.objects.all()