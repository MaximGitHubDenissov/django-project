from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = 'Get All Clients'

    def handle(self, *args, **options):
        clients = '\n'.join(f'{client}' for client in Client.objects.all())
        self.stdout.write(clients)
