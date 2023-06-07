from rest_framework import serializers
from .models import TimestampModel, Category, Product, User, ShoppingCart, CartItem, Order, OrderItem

class TimestampModelSerializers(serializers.ModelSerializer):
  class Meta:
    model = TimestampModel
    fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
  # category = CategorySerializers(read_only=True)
  class Meta:
    model = Product
    fields = '__all__'

  def validate_product_price(self, product_price):
    if product_price < 0:
      raise serializers.ValidationError("price cannot be negative.")
    return product_price
  
  def validate_product_weight(self, product_weight):
    if product_weight < 0:
      raise serializers.ValidationError("product weight cannot be negative.")
    return product_weight  

class UserSerializers(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

  def validate_phone(self, phone):
    if len(phone) < 11:
      raise serializers.ValidationError("phone number must consist of 11 digits.")
    return phone


class ShoppingCartSerializers(serializers.ModelSerializer):
  user = UserSerializers(read_only=True)
  class Meta:
    model = ShoppingCart
    fields = '__all__'


class CartItemSerializers(serializers.ModelSerializer):
  product = ProductSerializers(read_only=True)
  class Meta:
    model = CartItem
    fields = '__all__'

  def validate_quantity(self, quantity):
    if quantity < 0:
      raise serializers.ValidationError("quantity weight cannot be negative.")
    return quantity

class OrderSerializers(serializers.ModelSerializer):
  # user = UserSerializers(read_only=True)
  product = ProductSerializers(read_only=True)
  class Meta:
    model = Order
    fields = '__all__'

  def validate_total_amount(self, total_amount):
    if total_amount < 0:
      raise serializers.ValidationError("total amount cannot be negative.")
    return total_amount

class OrderItemSerializers(serializers.ModelSerializer):
  product = ProductSerializers(read_only=True)
  class Meta:
    model = OrderItem
    fields = '__all__'

  def validate_quantity(self, quantity):
    if quantity < 0:
      raise serializers.ValidationError("quantity weight cannot be negative")
    return quantity

  def validate_price(self, price):
    if price < 0:
      raise serializers.ValidationError("price cannot be negative.")
    return price