from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'total')


admin.site.register(Order, OrderAdmin)
