from django.shortcuts import render
from rest_framework import viewsets

from .models import Customer, Seller, Category, Product
from .serializers import CustomerSerialazer, SellerSerialazer , CategorySerializer, ProductSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerialazer
    queryset = Customer.objects.all()


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = SellerSerialazer
    queryset = Seller.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()

