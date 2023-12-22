import random
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework import status


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """
    ListCreateAPIView for Products.

    This view allows:
    - GET request to retrieve a list of all products.
    - POST request to create a new product.

    Endpoint:
    - GET: /api/products/
    - POST: /api/products/
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateDestroyAPIView for Products.

    This view allows:
    - GET request to retrieve details of a specific product.
    - PUT request to update details of a specific product.
    - DELETE request to delete a specific product.

    Endpoint:
    - GET: /api/products/<int:pk>/
    - PUT: /api/products/<int:pk>/
    - DELETE: /api/products/<int:pk>/
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({"id": user.id}, status=status.HTTP_200_OK)
