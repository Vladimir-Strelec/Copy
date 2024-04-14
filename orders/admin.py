from django.contrib import admin

from orders.models import Order, OrderItem

# admin.site.register(Order)
# admin.site.register(OrderItem)


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity", "id_for_order",
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity", "id_for_order",
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        "requires_delivery",
        "status",
        # "payment_on_get",
        "is_paid",
        "created_timestamp",
        "id_for_order",
    )

    search_fields = (
        "requires_delivery",
        # "payment_on_get",
        "is_paid",
        "created_timestamp",
        "id_for_order",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        # "requires_delivery",
        "status",
        # "payment_on_get",
        "is_paid",
        "created_timestamp",
        "id_for_order",
    )

    search_fields = (
        "id",
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (
        # "requires_delivery",
        "status",
        # "payment_on_get",
        "is_paid",
        "id_for_order",

    )
    inlines = (OrderItemTabulareAdmin,)
