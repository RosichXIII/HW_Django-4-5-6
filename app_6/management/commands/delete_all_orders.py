from django.core.management.base import BaseCommand
from app_6.models import Order

class Command(BaseCommand):
    help = 'Удаление всех заказов'

    def handle(self, *args, **kwargs):
        Order.objects.all().delete()
        print('Все заказы удалены')