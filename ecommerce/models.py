from django.db import models
from datetime import datetime
from django.utils import timezone

class TimestampModel(models.Model):
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(null=True)

  class Meta:
    abstract = True

class User(TimestampModel):
  user_name = models.CharField(max_length=255, null=False)
  email = models.EmailField(null=False)
  phone = models.CharField(max_length=12)
  address = models.CharField(max_length=100)
  zipcode = models.IntegerField(null= False)
  
  def __str__(self):
    return self.user_name


class Category(TimestampModel):
  category_name = models.CharField(max_length=255, null=False)
  description = models.TextField(max_length=100)
  category_type = models.TextField(max_length=100 , null=False)

  def __str__(self):
    return self.category_name


class Product(TimestampModel):
  product_name = models.CharField(max_length=255, null=False)
  product_description = models.TextField(max_length=200, null=False)
  product_price = models.IntegerField(default=0)
  product_weight = models.IntegerField(default=0)
  product_brand = models.CharField(max_length=20)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

  def __str__(self):
    return self.product_name


class ShoppingCart(TimestampModel):
  user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="shoppingcart")
  status = models.CharField(max_length=255)

  def __str__(self):
    return f"Shopping Cart : {self.id}"


class CartItem(TimestampModel):
  shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE , related_name="cartitem")
  product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name="cartitem")
  quantity = models.IntegerField(default=0)

  def __str__(self):
    return f"Cart Item : {self.id}"

class Order(TimestampModel):
  user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="order")
  total_amount = models.IntegerField(default=0)
  status = models.CharField(max_length=255)

  def __str__(self):
    return f"Order : {self.id}"


class OrderItem(TimestampModel):
  order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name="orderitem")
  product = models.ForeignKey(Product, on_delete=models.CASCADE ,related_name="orderitem")
  quantity = models.IntegerField(default=0)
  price = models.IntegerField(default=0)

  def __str__(self):
    return f"Order Item : {self.id}"