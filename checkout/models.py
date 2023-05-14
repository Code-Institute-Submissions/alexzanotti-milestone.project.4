import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from plans.models import Plan


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update order total each time a line item is added.
        """
        self.order_total = self.lineitem.plan_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class PlanOrder(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name='lineitem')
    plan = models.ForeignKey(
        Plan, null=False, blank=False, on_delete=models.CASCADE)
    plan_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the plan total
        and update the order total.
        """
        self.plan_total = self.plan.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.plan.name} (Plan ID {self.plan.id}) on order {self.order.order_number}'