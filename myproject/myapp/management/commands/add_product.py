from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Add Product'

    def handle(self, *args, **options):
        product = Product(name='Milk', description='Mu Mu', price=15.25)
        product.save()
        self.stdout.write(f'{product} created')