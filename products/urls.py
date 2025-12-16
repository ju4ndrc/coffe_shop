
from django.urls import path

from products.views import show_products

urlpatterns = [
    path("products_list/",show_products)
    
]
