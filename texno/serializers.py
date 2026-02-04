from rest_framework import serializers
from .models import Category, Product, Image, Order, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", 'name', 'slug', 'image', 'is_active']

class ProductSerializer(serializers.ModelSerializer):               # same-same but different
    class Meta:
        model = Product
        exclude = ()

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", 'name', 'description', 'price', 'category']

class ProductOfCategoryModelSerializer(serializers.ModelSerializer): # same-same but different
    class Meta:
        model = Product
        exclude = ()

class ImageSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source = 'product.name')
    class Meta:
        model = Image
        exclude = ()

class ImageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", 'product', 'image']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = () 

class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", 'payment_method', 'is_delivery', 'store_location', 'description', 'user', 'product']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = "__all__"
