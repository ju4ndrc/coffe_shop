
from django.urls import path

from products.views import ProductFormView, show_products

urlpatterns = [
    path("products_list/",show_products),
    
    path('add/',ProductFormView.as_view(),name='add_product'),
]
