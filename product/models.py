from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from enum import Enum


class Options(Enum):    
    DEFAULT_STATUS = 'Pending'
    CLOSED = 'Closed'


class MyUser(AbstractUser):
    phone_number = models.IntegerField(default=0, null=True)
    address = models.CharField(max_length=100, null=True)   

    def __str__(self):
        return f'{self.username}'

class Product(models.Model):    
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to="products_images", null=True, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):    
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name}'

class Cart(models.Model):
    date = models.DateTimeField(default=timezone.now, null=False)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    status = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.value) for tag in Options],
        default=Options.DEFAULT_STATUS.value 
    )

    def __str__(self):
        return f"{self.date} - {self.customer} - {self.status}" 

    @property
    def get_cart_total(self):
        print("geting cart total items")
        orderitems = self.cartitem_set.all()
        total = sum([item.get_total for item in orderitems])
        print(f"the total price for items is :{total}")
        return total
    
    @property
    def get_cart_items(self):
        print("geting cart items")
        orderitems = self.cartitem_set.all()
        total = sum([item.amount for item in orderitems])
        print(f"the total cart items num is: {total}")
        return total

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', related_name='cartitems', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', related_name='products', on_delete=models.CASCADE, null=True)
    quantity = models.FloatField(default=0)
    
    def __str__(self):
        return f'{self.id}'

    @property
    def get_total(self):
        print("calculate total price for item")
        total = self.product.price * self.quantity
        print(f"the total price for item is: {total}")
        return total

class GiftCard(models.Model):
   description = models.CharField(max_length=200)
   sum = models.IntegerField()
