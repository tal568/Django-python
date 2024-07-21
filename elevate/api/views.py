from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import productSerializer


# Create your views here.


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product(request, productId):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=productId)
        serializer = productSerializer(product)
        return Response(serializer.data)
    if request.method == 'DELETE':
        get_object_or_404(Product, id=productId).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        product = get_object_or_404(Product, id=productId)

        serializer = productSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
