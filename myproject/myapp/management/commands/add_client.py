from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = 'Add Client'

    def handle(self, *args, **options):
        client = Client(name='Peter', email='peter@test.com',
                        phone='777-888', address='Almaty')
        client.save()
        self.stdout.write(f'{client} created')


