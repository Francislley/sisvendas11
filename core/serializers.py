from rest_framework import serializers

from .models import Customer, Seller, Product, Sale, SaleDetail


class CustomerSerialazer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'name')


class SellerSerialazer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = ('id', 'name')