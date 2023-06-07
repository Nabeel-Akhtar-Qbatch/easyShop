from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'shoppingcart', views.ShoppingCartViewSet)
router.register(r'cartitem', views.CartItemViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'orderitem', views.OrderItemViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('api/product/create/', views.ProductCreateAPIView.as_view(), name='product-create'),
  path('api/user/create/', views.UserCreateAPIView.as_view(), name='user-create'),
  path('api/category/create/', views.CategoryCreateAPIView.as_view(), name='category-create'),
  path('api/order/confirm/', views.ConfirmOrderAPIView.as_view(), name='order-confirm'),
  path('api/user/details/<str:username>/', views.ConfirmOrderNameAPIView.as_view(), name='order-confirm'),
]