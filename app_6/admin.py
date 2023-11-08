from django.contrib import admin
from .models import *

@admin.register(Customer)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address", "registration_date"]
    ordering = ["name", "registration_date"]
    list_filter = ["registration_date"]
    search_fields = ["name", "phone"]
    search_help_text = "Поиск по полю имя клиента и номеру телефона"
    fields = ["name", "email", "phone", "address", "registration_date"]
    readonly_fields = ["registration_date"]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_description", "price", "product_quantity", "product_acceptance_date"]
    ordering = ["product_name", "-price"]
    list_filter = ["product_acceptance_date"]
    search_fields = ["product_name"]
    search_help_text = "Поиск по полю имя продукта"
    fieldsets = [
        (
            'Наименование продукта и его описание',
            {
                'classes': ['wide'],
                'fields': ['product_name', 'product_description'],
            },
        ),
        (
            'Цена за 1шт',
            {
                'product_description': 'Категория товара и его подробное описание',
                'fields': ['price'],
            },
        ),
        (
            'Дата поступления товара и количество',
            {
                'classes': ['collapse'],
                'product_description': 'Дата и количество',
                'fields': ['product_acceptance_date', 'product_quantity'],
            }
        ),
    ]
    readonly_fields = ["product_acceptance_date"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "price_total_order", "date_order"]
    ordering = ["customer", "date_order"]
    list_filter = ["date_order"]
    search_fields = ["customer"]
    search_help_text = "Поиск по полю имя продукта по ID клиента"
    fields = ["customer", "price_total_order", "date_order", "products"]
    readonly_fields = ["date_order"]
