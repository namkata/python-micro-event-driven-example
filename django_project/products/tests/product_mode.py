from django.test import TestCase
from ..models import Product


class ProductModelTest(TestCase):
    def setUp(self):
        self.product_data = {
            "title": "Test Product",
            "image": "test_image.jpg",
            "likes": 10,
        }

    def test_create_product(self):
        product = Product.objects.create(**self.product_data)
        self.assertEqual(product.title, self.product_data["title"])
        self.assertEqual(product.image, self.product_data["image"])
        self.assertEqual(product.likes, self.product_data["likes"])
