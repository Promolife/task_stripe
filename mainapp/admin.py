from django.contrib import admin
from .models import Item, ItemOrder, Order, Discount, Tax


class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'description',
                    'price',
                    )
    search_fields = ('name',)
    list_filter = ('name', 'price')
    list_editable = ('price',)
    empty_value_display = '-пусто-'


class ItemOrderAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'item',
                    'order',
                    'created',
                    )
    empty_value_display = '-пусто-'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'description',
                    )
    search_fields = ('description',)
    empty_value_display = '-пусто-'


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'description',
                    'amount',
                    'stripe_id'
                    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class TaxAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'amount',
                    'description',
                    'txr',
                    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemOrder, ItemOrderAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Tax, TaxAdmin)
