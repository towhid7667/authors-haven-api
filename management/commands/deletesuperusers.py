from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Deletes all superuser accounts'

    def handle(self, *args, **options):
        superusers = User.objects.filter(is_superuser=True)
        for superuser in superusers:
            print(f'Deleting superuser: {superuser.username}')
            superuser.delete()
        print('All superusers have been deleted.')
