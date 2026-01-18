from django.shortcuts import render
from django.views import generic

from django.urls import reverse_lazy
from products.forms import ProductForm
from products.models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.response import Response
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



class ProductListAAPI(APIView):
    #permisos

    authentication_classes = []
    permission_classes = []
    def get(self,request):
        products = Product.object.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)