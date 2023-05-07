import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings


# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=255, unique=True, editable=False)
    user_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)

    def __str__(self):
        return f'Order {self.order_number}'
