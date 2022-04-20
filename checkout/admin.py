from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    """ The Adminclass for the OrderLineItem Model"""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ The Adminclass for the Order Model"""
    inlines = (OrderLineAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'total_cost',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'street_address1',
              'street_address2', 'postcode', 'county',
              'town_or_city', 'country', 'delivery_cost',
              'order_total', 'total_cost',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'total_cost',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
