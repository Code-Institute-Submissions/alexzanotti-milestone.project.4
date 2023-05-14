from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_item = []
    order_total = 0

    context = {
        'bag_item': bag_item,
        'order_total': order_total,
    }

    return context
