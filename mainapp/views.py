import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Item, Order
from .stripes import (
    stripe_session_create_helper,
    stripe_check_or_create_tax,
    stripe_check_or_create_discount
)


def item_detail(request, item_id):
    template = 'mainapp/simple.html'
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
        'token': os.getenv('PK_TOKEN')
    }
    return render(request, template, context)


def buy_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    session = stripe_session_create_helper(
        item.name,
        item.price,
        None,
        None
    )
    return HttpResponse(JsonResponse({'sessionId': session.id}))


def order_detail(request, order_id):
    template = 'mainapp/orders.html'
    sum_price = 0
    order = get_object_or_404(Order, pk=order_id)
    items = order.items.all()
    for item in items:
        sum_price += item.price
    context = {
        'order': order,
        'items': items,
        'price': sum_price,
        'token': os.getenv('PK_TOKEN')
    }
    return render(request, template, context)


def buy_order(request, order_id):
    stripe_check_or_create_discount()
    stripe_check_or_create_tax()
    sum_price = 0
    tax_txr = None
    discount = None
    order = get_object_or_404(Order, pk=order_id)
    items = order.items.all()
    if order.tax:
        tax_txr = order.tax.txr
    if order.discount:
        discount = order.discount.stripe_id
    for item in items:
        sum_price += item.price
    session = stripe_session_create_helper(
        order.description,
        sum_price,
        tax_txr,
        discount
    )
    return HttpResponse(JsonResponse({'sessionId': session.id}))
