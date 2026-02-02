from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Image
from texno import serializers
from django.core.cache import cache
from django.shortcuts import get_object_or_404


# 1) Category uchun API chiqarasiz. CRUD => 
class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryListAPIView(APIView):
    def get(self, request):
        # cache_key = 'category_list'
        # data = cache.get(cache_key)

        # if data is None:
        queryset = Category.objects.all()
        serializer = serializers.CategorySerializer(queryset, many=True)
        data = serializer.data
            # cache.set(cache_key, data, 60*5)
        
        return Response(data)


class CategoryUpdateAPIView(APIView):
    def put(self, request, category_id=None):
        category = get_object_or_404(Category, id=category_id)

        serializer = serializers.CategoryUpdateSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"not valid", "details": serializer.errors})
        
    def patch(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)

        serializer = serializers.CategoryUpdateSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteAPIView(APIView):
    def delete(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# 2) Product uchun=> CRUD => 
class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductListAPIView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = serializers.ProductSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)


class ProductUpdateAPIView(APIView):
    def put(self, request, product_id=None):
        product = get_object_or_404(Product, id=product_id)

        serializer = serializers.ProductUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"not valid", "details": serializer.errors})
        
    def patch(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)

        serializer = serializers.ProductUpdateSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteAPIView(APIView):
    def delete(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 3) Categoryga tegishli productlar
class ProductByCategory(APIView):
    def get(self, request, slug):
        category_id = Category.objects.get(slug=slug).id
        product = Product.objects.filter(category=category_id)
        serializer = serializers.ProductOfCategoryModelSerializer(product, many=True)
        data = serializer.data
        return Response(data)
        

# 4) Image uchun Api chiqarasiz.
class ImageCreateAPIView(CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer


class ImageListAPIView(APIView):
    def get(self, request):
        queryset = Image.objects.all()
        serializer = serializers.ImageSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)
