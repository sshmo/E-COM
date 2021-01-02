from django.shortcuts import render

from rest_framework import generics
from .models import User, Product, Customer, Comment
from .serializers import UserSerializer, ProductSerializer, CustomerSerializer, CommentSerializer


class ListUser(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListProduct(generics.ListCreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListCustomer(generics.ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DetailCustomer(generics.RetrieveUpdateDestroyAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ListComment(generics.ListCreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class DetailComment(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
