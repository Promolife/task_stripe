from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('buy/<int:item_id>/', views.buy_item, name='buy_item'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    path('orders/buy/<int:order_id>/', views.buy_order, name='buy_order'),
]
