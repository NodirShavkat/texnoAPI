from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import status
from .models import Category, Product, Image, Order, Comment
from texno import serializers
from django.core.cache import cache
from django.shortcuts import get_object_or_404


# 1) Category uchun API chiqarasiz. CRUD => 
class CategoryCreateAPIView(CreateAPIView):
    permission_classes = [IsAdminUser] # is_staff=True bo'lganlar view dan foydalana oladi
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryListAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        cache_key = 'category_list' # Cache added
        cached_data = cache.get(cache_key)

        if not cached_data:
            queryset = Category.objects.all()
            serializer = serializers.CategorySerializer(queryset, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=3600)
            return Response(data)
        return Response(cached_data)


class CategoryUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]

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
    permission_classes = [IsAdminUser]
    
    def delete(self, request, category_id):
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# 2) Product uchun=> CRUD => 
class ProductCreateAPIView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer


class ProductListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Product.objects.all()
        serializer = serializers.ProductSerializer(queryset, many=True)
        data = serializer.data
        return Response(data)


class ProductUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]
    
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
    permission_classes = [IsAdminUser]
    
    def delete(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 3) Categoryga tegishli productlar
class ProductByCategory(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        category_id = Category.objects.get(slug=slug).id
        product = Product.objects.filter(category=category_id)
        serializer = serializers.ProductOfCategoryModelSerializer(product, many=True)
        data = serializer.data
        return Response(data)
        

# 4) Image uchun Api chiqarasiz.
class ImageCreateAPIView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer


# class ImageListAPIView(APIView): # <- APIView Pagination bilan ishlamas ekan
#     permission_classes = [AllowAny]

#     def get(self, request):
#         queryset = Image.objects.all()
#         serializer = serializers.ImageSerializer(queryset, many=True)
#         data = serializer.data
#         return Response(data)
    
class ImageListAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = serializers.ImageSerializer
    permission_classes = [AllowAny]

    def get_queryset(self): # Query Optimization
        return Image.objects.select_related('product').all()
    

class ImageUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]
    
    def put(self, request, image_id=None):
        image = get_object_or_404(Image, id=image_id)

        serializer = serializers.ImageUpdateSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"not valid", "details": serializer.errors})
        
    def patch(self, request, image_id):
        image = get_object_or_404(Image, id=image_id)

        serializer = serializers.ImageUpdateSerializer(image, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]
    
    def delete(self, request, image_id):
        image = get_object_or_404(Image, id=image_id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 5) Product ga tegishli Imagelar
class ImageByProduct(APIView):
    permission_classes = [AllowAny]

    def get(self, request, product_id):
        images = Image.objects.filter(product=product_id)
        serializer = serializers.ImageSerializer(images, many=True)
        data = serializer.data
        return Response(data)
    

# 6) Order lar uchun API
class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAdminUser] 

    def get_queryset(self): # Query Optimization
        return Order.objects.select_related('product').all()
    
# Authentifikatsiyadan o'tgan user faqat o'zini orderlarini ko'ra oladigan view qilish kerak


class OrderUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated | IsAdminUser]
    
    def put(self, request, order_id=None):
        order = get_object_or_404(Order, id=order_id)

        serializer = serializers.OrderUpdateSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message":"not valid", "details": serializer.errors})
        
    def patch(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)

        serializer = serializers.OrderUpdateSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]
    
    def delete(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 7) Commentslar uchun
class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CommentListAPIView():
    pass


class CommentUpdateAPIView():
    pass


class CommentDeleteAPIView():
    pass


# 8) Productga tegishli comments
class CommentByProduct(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, product_id):
        comment = Comment.objects.filter(product=product_id)
        serializer = serializers.CommentSerializer(comment, many=True)
        data = serializer.data
        return Response(data)
  
  