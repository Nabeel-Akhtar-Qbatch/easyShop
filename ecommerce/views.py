from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from .models import Category, Product, User, ShoppingCart, CartItem, Order, OrderItem
from django.db.models import Prefetch
from .serializers import CategorySerializers, ProductSerializers, UserSerializers, ShoppingCartSerializers, CartItemSerializers, OrderSerializers, OrderItemSerializers 

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializers

  lookup_field = 'category_name'

  def retrieve(self, request, **kwargs):
    category_name = kwargs['category_name']
    instance = get_object_or_404(Category, category_name=category_name)
    serializer = self.get_serializer(instance)
    return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers

  def list(self, request, **kwargs):
    queryset = self.get_queryset()
    serializer = self.get_serializer(queryset, many=True)

    total_price_sum = sum(product.product_price for product in queryset)
    response_data = {
      'results': serializer.data,
      'total_price_sum': total_price_sum
    }

    return Response(response_data)
  
  lookup_field = 'product_name'

  def retrieve(self, request, **kwargs):
    product_name = kwargs['product_name']
    instance = get_object_or_404(Product, product_name=product_name)
    serializer = self.get_serializer(instance)
    return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    lookup_field = 'user_name'

    def retrieve(self, request, **kwargs):
      user_name = kwargs['user_name']
      instance = get_object_or_404(User, user_name=user_name)
      serializer = self.get_serializer(instance)
      return Response(serializer.data)


class ShoppingCartViewSet(viewsets.ModelViewSet):
  queryset = ShoppingCart.objects.all()
  serializer_class = ShoppingCartSerializers

class CartItemViewSet(viewsets.ModelViewSet):
  queryset = CartItem.objects.all()
  serializer_class = CartItemSerializers

class OrderViewSet(viewsets.ModelViewSet):
  queryset = Order.objects.all()
  serializer_class = OrderSerializers

class OrderItemViewSet(viewsets.ModelViewSet):
  queryset = OrderItem.objects.all()
  serializer_class = OrderItemSerializers


class ProductCreateAPIView(APIView):
  def post(self, request):
    data = request.data
    if isinstance(data, list):
      response_data = []
      for item in data:
        category_name = item.get('category')
        if category_name is None:
          return Response({'error': 'category is required'}, status=400)

        category, created = Category.objects.get_or_create(category_name=category_name, description=item.get('description'), category_type=item.get('category_type'))
        serializer = ProductSerializers(data=item)
        if serializer.is_valid():
          serializer.save(category=category)
          response_data.append(serializer.data)
        else:
          return Response(serializer.errors, status=400)

      return Response(response_data, status=201)
    


class UserCreateAPIView(APIView):
  def post(self, request):
    data = request.data
    if isinstance(data, list):
      response_data = []
      for item in data:
        serializer = UserSerializers(data=item)
        if serializer.is_valid():
          serializer.save()
          response_data.append(serializer.data)
        else:
          return Response(serializer.errors, status=400)
      return Response(response_data, status=201)
    else:
      serializer = UserSerializers(data=data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
      return Response(serializer.errors, status=400)

class CategoryCreateAPIView(APIView):
  def post(self, request):
    data = request.data
    if isinstance(data, list):
      response_data = []
      for item in data:
        serializer = CategorySerializers(data=item)
        if serializer.is_valid():
          serializer.save()
          response_data.append(serializer.data)
        else:
          return Response(serializer.errors, status=400)

      return Response(response_data, status=201)
    
    else:
      serializer = CategorySerializers(data=data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
      return Response(serializer.errors, status=400)


class ConfirmOrderAPIView(APIView):
  def post(self, request):
    orders = Order.objects.filter(status='Confirm')
    order_items = OrderItem.objects.filter(order__in=orders)
    total_price, order_details = 0, []
    for order in orders:
      order_items = order.orderitem.all()
      order_item_details, order_total_price = [], 0
      for item in order_items:
        item_total_price = item.quantity * item.price
        order_total_price += item_total_price
        order_item_details.append({
          'product': item.product.product_name,
          'quantity': item.quantity,
          'price': item.price,
          'total_price': item_total_price
        })
      total_price += order_total_price
      order_details.append({
          'order_id': order.id,
          'user': order.user.user_name,
          'status': order.status,
          'order_items': order_item_details,
      })
    response_data = {
      'order_details': order_details,
      'total_price': total_price,
      'total_orders': len(order_details)
    }
    return Response(response_data)


class ConfirmOrderNameAPIView(APIView):
    def get(self, request, username):
      user = get_object_or_404(User, user_name=username)
      user_serializer = UserSerializers(user)

      orders = Order.objects.filter(user=user, status='Confirm')
      order_serializer = OrderSerializers(orders, many=True)

      response_data = {
        'user': user_serializer.data,
        'orders': []
      }

      for order in orders:
        order_data = OrderSerializers(order).data

        products = Product.objects.filter(orderitem__order=order)
        product_serializer = ProductSerializers(products, many=True)
        order_data['products'] = product_serializer.data

        categories = Category.objects.filter(products__in=products).distinct()
        category_serializer = CategorySerializers(categories, many=True)
        order_data['categories'] = category_serializer.data

        response_data['orders'].append(order_data)

      return Response(response_data)