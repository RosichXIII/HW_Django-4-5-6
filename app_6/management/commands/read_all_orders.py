from django.core.management.base import BaseCommand
from app_6.models import Order

class Command(BaseCommand):
    help = 'Вывод всех заказов'

    def handle(self, *args, **kwargs):
        order = Order.objects.all()
        print(order)