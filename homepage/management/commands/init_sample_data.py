from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


def create_address_and_associated_letting(number, street, city, state, zip_code,
                                          country_iso_code, letting_title):
    address = Address.objects.create(
        number=number, street=street, city=city, state=state, zip_code=zip_code,
        country_iso_code=country_iso_code
    )
    address.save()
    letting = Letting.objects.create(title=letting_title, address=address)
    letting.save()


def create_user_and_associated_profile(username, password, email, first_name,
                                       last_name, profile_favorite_city):
    user = User.objects.create(
        username=username, password=password, email=email,
        first_name=first_name, last_name=last_name, is_staff=False, is_superuser=False)
    user.save()
    profile = Profile.objects.create(user=user, favorite_city=profile_favorite_city)
    profile.save()


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        admin_user = User.objects.create(
            username="admin", password="Abc1234!", email="admin@test.com",
            first_name="admin", last_name='admin', is_staff=True, is_superuser=True)
        admin_user.save()
