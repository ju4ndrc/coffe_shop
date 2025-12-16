from django.shortcuts import render

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