from django.urls import path
from products.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, UserAPIView

urlpatterns = [
    path('products', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('user', UserAPIView.as_view()),
]