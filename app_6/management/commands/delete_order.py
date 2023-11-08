from django.core.management.base import BaseCommand
from app_6.models import Order

class Command(BaseCommand):
    help = 'Удаления заказа, указав ID заказа'

    def add_arguments(self, parser):
        parser.add_argument('id_order', type=int)

    def handle(self, *args, **kwargs):
        id_order = kwargs['id_order']
        Order.objects.filter(pk=id_order).delete()
        print('Заказ удалён')
