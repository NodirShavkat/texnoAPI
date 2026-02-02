from rest_framework import serializers
from .models import Category, Product, Image

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ()

class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", 'name', 'slug', 'image', 'is_active']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", 'name', 'description', 'price', 'category']

class ProductOfCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ()

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ()
