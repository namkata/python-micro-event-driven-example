from django.test import TestCase
from ..models import Product
from ..serializers import ProductSerializer


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.product_data = {
            "title": "Test Product",
            "image": "test_image.jpg",
            "likes": 10,
        }
        self.product = Product.objects.create(
            title="Existing Product", image="existing_image.jpg", likes=5
        )

    def test_product_serializer_with_valid_data(self):
        serializer = ProductSerializer(data=self.product_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

    def test_product_serializer_with_invalid_data(self):
        invalid_data = {"title": "Test Product"}
        serializer = ProductSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertTrue("image" in serializer.errors)
