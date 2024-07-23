from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('products', views.product_list, name='products'),
    path('product/<int:productId>', views.product, name='product'),
    path('register', views.register, name='register'),
    path('login', obtain_auth_token, name='login'),

]
