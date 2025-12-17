from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy
from products.forms import ProductForm
from products.models import Product

# Create your views here.


class ProductFormView(generic.FormView):
    template_name = 'products/add_products.html'
    form_class = ProductForm
    success_url = reverse_lazy('products_list')

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

class ShowProducts(generic.ListView):
    
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'



