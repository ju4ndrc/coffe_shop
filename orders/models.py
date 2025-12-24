import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    is_active = models.BooleanField(default=True)
    orderDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order id {self.id} by {self.user}'
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order)