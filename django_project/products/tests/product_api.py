from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Product
from ..serializers import ProductSerializer


class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product_data = {
            "title": "Test Product",
            "image": "test_image.jpg",
            "likes": 10,
        }
        self.product = Product.objects.create(
            title="Existing Product", image="existing_image.jpg", likes=5
        )

    def test_get_all_products(self):
        response = self.client.get(reverse("product-list-create"))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_product(self):
        response = self.client.post(reverse("product-list-create"), self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Product.objects.count(), 2
        )  # Assuming there's one existing product

    def test_get_single_product(self):
        response = self.client.get(reverse("product-detail", args=[self.product.id]))
        serializer = ProductSerializer(self.product)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_product(self):
        updated_data = {
            "title": "Updated Product",
            "image": "updated_image.jpg",
            "likes": 15,
        }
        response = self.client.put(
            reverse("product-detail", args=[self.product.id]), updated_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.title, updated_data["title"])

    def test_delete_product(self):
        response = self.client.delete(reverse("product-detail", args=[self.product.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
