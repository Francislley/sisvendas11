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
        return self.nome


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
