from django.urls import reverse_lazy
from django.views.generic import DetailView,CreateView
from django.views import generic
from orders.forms import OrderProductForm
from products.models import Product
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MyOrderView(LoginRequiredMixin,DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset = None):
        return Order.objects.filter(is_active = True, user = self.request.user).first()
    
class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/product.html'   
    context_object_name = 'products'
    
class CreateOrderProductView(LoginRequiredMixin,CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy('my_order')
    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active = True,
            user = self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        super().form_valid(self,form)