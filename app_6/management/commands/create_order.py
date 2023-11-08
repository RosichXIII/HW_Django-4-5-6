from django.core.management.base import BaseCommand
from app_6.models import *

class Command(BaseCommand):
    help = 'Создание заказа, указав аргументы через пробел: первое значение - ID клиента, последующие - ID товаров'

    def add_arguments(self, parser):
        parser.add_argument('user', type=int)
        parser.add_argument('prod', nargs='+', type=int)

    def handle(self, *args, **kwargs):
        user = kwargs['user']
        prod = kwargs['prod']
        sum = 0
        cli = Customer.objects.get(pk=user)
        order = Order.objects.create(customer=cli, price_total_order=sum)
        for i in prod:
            order.products.add(Product.objects.get(pk=i))
            sum += Product.objects.get(pk=i).price
            order.save()
        order.price_total_order = sum
        order.save()
