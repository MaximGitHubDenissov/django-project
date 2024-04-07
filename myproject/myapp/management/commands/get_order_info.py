from django.core.management.base import BaseCommand
from myapp.models import Order, Enrollment


class Command(BaseCommand):
    help = 'Get information from Order'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        enrolls = Enrollment.objects.filter(order=order).all()
        products = '\n'.join(f'{enroll.product.name} {enroll.quantity}' for enroll in enrolls)
        self.stdout.write(f'{products}\nTotal:{order.total_order} \n {order.date_ordered}')
