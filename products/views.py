from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy
from products.forms import ProductForm
from products.models import Product

# Create your views here.

def show_products(request,*args,**kwargs):
    print(args)
    print(kwargs)
    get_products = Product.objects.all()
    context = {
        "products":get_products
    }
    return render(request,"products/products.html",context)

class ProductFormView(generic.FormView):
    template_name = 'products/add_products.html'
    form_class = ProductForm
    success_url = reverse_lazy('add_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)