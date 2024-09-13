from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render
from django.views import View


class ProductListAPIView(generics.ListAPIView):
    """Класс получения списка всех продуктов в формате json"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreateAPIView(generics.CreateAPIView):
    """Класс Создания продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductView(View):
    """Класс для отображения страницы с продуктами"""
    def get(self, request, *args, **kwargs):
        return render(request, 'products/products_page.html')
