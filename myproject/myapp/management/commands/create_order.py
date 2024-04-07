import datetime

from django.core.management.base import BaseCommand
from myapp.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Create Order'

    def add_arguments(self, parser):
        parser.add_argument('client', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['client']
        client = Client.objects.filter(pk=pk).first()
        order = Order(client=client,
                      total_order=0,
                      date_ordered=datetime.datetime(2024, 1, 1))
        order.save()
        self.stdout.write(f'Created {order}')
