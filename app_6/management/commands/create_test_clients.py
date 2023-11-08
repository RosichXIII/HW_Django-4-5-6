from django.core.management.base import BaseCommand
from app_6.models import Customer

class Command(BaseCommand):
    help = 'Создание тестовых клиентов'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        
        for i in range(1, count + 1):
            customer = Customer(name=f'Cool_name{i}',
                            email=f'somemail{i}@gmail.com',
                            phone=f'{8888000 + i}',
                            address=f'anywhere_{i}')
            customer.save()