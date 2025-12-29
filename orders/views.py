from django.urls import reverse_lazy
from django.views.generic import DetailView,CreateView

from orders.forms import OrderProductForm
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MyOrderView(LoginRequiredMixin,DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset = None):
        return Order.objects.filter(is_active = True, user = self.request.user).first()
    
class CreateOrderProductView(CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    success_url = reverse_lazy('my_order')
