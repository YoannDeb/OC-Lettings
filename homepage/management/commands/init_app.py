from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        admin_user = User.objects.create(
            username="Admin", password="Abc1234!", email="admin@test.com",
            first_name="admin", last_name='admin', is_staff=True, is_superuser=True)
        admin_user.save()
