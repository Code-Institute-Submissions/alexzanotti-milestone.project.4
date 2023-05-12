from django.contrib import admin
from .models import Order, PlanOrder


class PlanOrderInline(admin.TabularInline):  # or admin.StackedInline
    model = PlanOrder
    readonly_fields = ('order', 'plan_total')


class OrderAdministration(admin.ModelAdmin):
    inlines = (PlanOrderInline,)

    readonly_fields = ('order_number', 'user_name',
                       'email', 'phone_number', 'date', 'order_total')


admin.site.register(Order, OrderAdministration)
