from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the product title")
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

    # Metadata
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-id"]

    def __str__(self):
        return self.title
