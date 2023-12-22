from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image",
        "likes",
    )  # Customize the displayed fields in the admin list view
    search_fields = ("title",)  # Enable searching by title in the admin interface
    list_filter = ("likes",)  # Add filters for 'likes' field in the admin interface
