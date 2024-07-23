
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

# Create your views here.


@api_view(['GET', 'POST'])
@login_required(login_url='login')
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    if request.method == 'DELETE':
        get_object_or_404(Product, id=product_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'PUT':
        product = get_object_or_404(Product, id=product_id)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url='login')
@api_view(['GET'])
def add_to_admin(request):
    if request.user.groups.filter(name='admin').exists():
        group = Group.objects.get(name='admin')
        group.user_set.add(request.user)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_200_OK)



@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user=serializer.save()
        token = Token.objects.create(user=user).key
        return Response({'user':serializer.data, 'token': token}, status=status.HTTP_201_CREATED, headers={'Authorization': 'Token ' + token})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
