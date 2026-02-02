from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryListAPIView.as_view()),
    path('category/create', views.CategoryCreateAPIView.as_view()),
    path('category/update/<int:category_id>/', views.CategoryUpdateAPIView.as_view()),
    path('category/delete/<int:category_id>/', views.CategoryDeleteAPIView.as_view()),
    
    path('product', views.ProductListAPIView.as_view()),
    path('product/create', views.ProductCreateAPIView.as_view()),
    path('product/update/<int:product_id>/', views.ProductUpdateAPIView.as_view()),
    path('product/delete/<int:product_id>/', views.ProductDeleteAPIView.as_view()),

    path('category/<slug:slug>/', views.ProductByCategory.as_view()),

    path('image', views.ImageListAPIView.as_view()),
    path('image/create', views.ImageCreateAPIView.as_view()),
]
