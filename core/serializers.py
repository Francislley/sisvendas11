from rest_framework import serializers

from .models import Customer, Seller, Product, Sale, SaleDetail, Category


class CustomerSerialazer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class SellerSerialazer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                       write_only=True,
                                                       source='categories', many=True)

    class Meta:
        model = Product
        fields = '__all__'