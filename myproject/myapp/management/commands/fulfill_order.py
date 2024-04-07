from django.core.management.base import BaseCommand
from myapp.models import Order, Product, Enrollment


class Command(BaseCommand):
    help = 'Fulfill Order <order_id> <product_id> <product_qnt>'


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
        enroll = Enrollment(order=order, product=product, quantity=qnt)
        enroll.save()
        order.total_order += product.price * qnt
        order.save()
        self.stdout.write(f'Add {qnt} {product.name} to {order}')
