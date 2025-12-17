
from django.urls import path

from products.views import ProductFormView, ShowProducts

urlpatterns = [
    path("list/",ShowProducts.as_view(),name='products_list'),
    
    path('add/',ProductFormView.as_view(),name='add_product'),
]
