
from django.urls import path

from products.views import ProductFormView, ShowProducts,ProductListAAPI

urlpatterns = [
    path("list/",ShowProducts.as_view(),name='products_list'),
    
    path('add/',ProductFormView.as_view(),name='add_product'),

    path('api/',ProductListAAPI.as_view(), name='list_product_api'),
]