from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer


# Create your views here.
class CartItemsViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, id=None):
        item = CartItem.objects.get(id=id)
        # Here we are passing three arguments to our serializer.
        # The instance of the CartItem model that we want to update.
        # The data received from the request.
        # partial=True to indicate that this may not contain all the fields of our model CartItem.
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})
        else:
            return Response({"status":"error", "data": serializer.errors})
