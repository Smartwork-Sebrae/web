from django.contrib import admin

from order.models import Order, OrderDesk


class OrderAdmin(admin.ModelAdmin):
    pass


class OrderDeskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDesk, OrderDeskAdmin)
