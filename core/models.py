from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Person(TimeStampedModel):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name


class Customer(Person):
    pass


class Seller(Person):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.product


class Sale(TimeStampedModel):
    customer = models.ForeignKey('Customer', related_name='customer_sale')
    seller = models.ForeignKey('Seller', related_name='seller_sale')
    
    def __str__(self):
        return self.created


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, related_name='sales_det')
    product = models.ForeignKey(Product, related_name='product_det')
    quantity = models.PositiveSmallIntegerField()
    price_sale = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def get_subtotal(self):
        return self.price_sale * (self.quantity or 0)

    subtotal = property(get_subtotal)
