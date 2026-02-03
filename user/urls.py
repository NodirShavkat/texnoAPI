from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('sample/', views.SampleView.as_view(), name='sample'),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('register/', views.UserRegisterationView.as_view(), name='register'),
    path('users/', views.UserListAPIView.as_view()),
]
