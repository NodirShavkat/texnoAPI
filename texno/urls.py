from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoryListAPIView.as_view()),#
    path('category/create', views.CategoryCreateAPIView.as_view()),#
    path('category/update/<int:category_id>/', views.CategoryUpdateAPIView.as_view()),#
    path('category/delete/<int:category_id>/', views.CategoryDeleteAPIView.as_view()),#
    
    path('product', views.ProductListAPIView.as_view()),#
    path('product/create', views.ProductCreateAPIView.as_view()),#
    path('product/update/<int:product_id>/', views.ProductUpdateAPIView.as_view()),#
    path('product/delete/<int:product_id>/', views.ProductDeleteAPIView.as_view()),#
    path('category/<slug:slug>/', views.ProductByCategory.as_view()), #

    path('image', views.ImageListAPIView.as_view()),#
    path('image/create', views.ImageCreateAPIView.as_view()),#
    path('image/<int:product_id>/', views.ImageByProduct.as_view()),#
    path('image/update/<int:image_id>/', views.ImageUpdateAPIView.as_view()),#
    path('image/delete/<int:image_id>/', views.ImageDeleteAPIView.as_view()),#

    path('order/create', views.OrderCreateAPIView.as_view()),
    path('order', views.OrderListAPIView.as_view()),
    path('order/update/<int:order_id>/', views.OrderUpdateAPIView.as_view()),
    path('order/delete/<int:order_id>/', views.OrderDeleteAPIView.as_view()), #

    path('comment/<int:product_id>/', views.CommentByProduct.as_view()),
    path('comment/create', views.CommentCreateAPIView.as_view()),
    path('comment', views.CommentListAPIView.as_view()),
    path('comment/update/<int:comment_id>/', views.CommentUpdateAPIView.as_view()),
    path('comment/delete/<int:comment_id>/', views.CommentDeleteAPIView.as_view()),

]
