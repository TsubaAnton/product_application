from django.urls import path
from .views import ProductListAPIView, ProductCreateAPIView, ProductView
from .apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductView.as_view(), name='products_page'),
    path('products/', ProductListAPIView.as_view(), name='products_list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='products_create')
]
