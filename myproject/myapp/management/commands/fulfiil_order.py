from django.core.management.base import BaseCommand
from myapp.models import Order, Product


class Command(BaseCommand):
    help = 'Fulfill Order'


    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('product', type=int, help='Product ID')
        parser.add_argument('qnt', type=int, help='Product Quantity')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        prod_id = kwargs['product']
        qnt = kwargs['qnt']
        product = Product.objects.filter(pk=prod_id).first()
        order = Order.objects.filter(pk=pk).first()
        order.products.add(product)
        order.total_order += product.price * qnt
        order.save()
        self.stdout.write(f'Add {qnt} {product.name} to {order}')
