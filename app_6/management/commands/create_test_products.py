from django.core.management.base import BaseCommand
from app_6.models import Product
from random import randint

class Command(BaseCommand):
    help = 'Создание тестовых товаров'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(product_name=f'Awesomestuff_{i}',
                              product_description=f'Lorem ipsum {i}',
                              price=f'{i + randint(7, 36)}',
                              product_quantity=f'{i+ randint(5, 26)}')
            product.save()