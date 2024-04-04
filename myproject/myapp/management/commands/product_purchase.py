from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Add Product To Store'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('qnt', type=int, help='Quantity of Product')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        qnt = kwargs['qnt']
        product = Product.objects.filter(pk=pk).first()
        product.quantity += qnt
        product.save()
        self.stdout.write(f'Add to store {qnt} {product.name}. Total {product.quantity}')


