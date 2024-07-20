from django.urls import path

from . import views

urlpatterns=[
    path('products',views.product_list,name='products'),
    path('delete_product/<int:productId>',views.delete_product,name='delete_product')
]