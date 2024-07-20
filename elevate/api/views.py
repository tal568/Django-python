from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import productSerializer
# Create your views here.




@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products=Product.objects.all()
        serializer=productSerializer(products,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer=productSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

    
@api_view(['DELETE'])
def delete_product(request,productId):
    count=get_object_or_404(Product,id=productId).delete()
    return Response({'deleted':count[0]})

