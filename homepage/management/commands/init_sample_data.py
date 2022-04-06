from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


def create_address_and_associated_letting(number, street, city, state, zip_code,
                                          country_iso_code, letting_title):
    if not Address.objects.filter(
            number=number, street=street, city=city, state=state, zip_code=zip_code, country_iso_code=country_iso_code
    ).exists():
        address = Address.objects.create(
            number=number, street=street, city=city, state=state, zip_code=zip_code,
            country_iso_code=country_iso_code
        )
        address.save()
    else:
        address = Address.objects.get(number=number, street=street, city=city, state=state, zip_code=zip_code,
                                      country_iso_code=country_iso_code)

    if not Letting.objects.filter(title=letting_title, address=address).exists():
        letting = Letting.objects.create(title=letting_title, address=address)
        letting.save()


def create_user_and_associated_profile(username, email, first_name,
                                       last_name, profile_favorite_city):
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(
            username=username, password="Abc1234!", email=email,
            first_name=first_name, last_name=last_name)
        user.save()
    else:
        user = User.objects.get(username=username)

    if not Profile.objects.filter(user=user.pk, favorite_city=profile_favorite_city).exists():
        profile = Profile.objects.create(user=user, favorite_city=profile_favorite_city)
        profile.save()


class Command(BaseCommand):
    help = 'Initiate sample database for deployment'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_user('admin', password='Abc1234!')
            admin_user.is_superuser = True
            admin_user.is_staff = True
            admin_user.save()

        create_address_and_associated_letting(7217, "Bedford Street", "Brunswick", "GA", 31525, "USA",
                                              "Joshua Tree Green Haus /w Hot Tub")
        create_address_and_associated_letting(4, "Military Street", "Willoughby", "OH", 44094, "USA",
                                              "Oceanview Retreat")
        create_address_and_associated_letting(340, "Wintergreen Avenue", "Newport News", "VA", 23601, "USA",
                                              "'Silo Studio' Cottage")
        create_address_and_associated_letting(9230, "E. Joy Ridge Street", "Marquette", "MI", 49855, "USA",
                                              "Pirates of the Caribbean Getaway")
        create_address_and_associated_letting(9606, "Harvard Street", "Aliquippa", "PA", 15001, "USA",
                                              "The Mushroom Dome Retreat & LAND of Paradise Suite")
        create_address_and_associated_letting(588, "Argyle Avenue", "East Meadow", "NY", 11554, "USA",
                                              "Underground Hygge")

        create_user_and_associated_profile("HeadlinesGazer", "jssssss33@acee9.live", "Jamie", "Lal", "Buenos Aires")
        create_user_and_associated_profile("DavWin", "5houssam.kessaiso@facpidif.ml", "Grahm", "Cassandra", "Barcelona")
        create_user_and_associated_profile("AirWow", "flocation.vam4@glendenningflowerdesign.com", "Ada", "Paul",
                                           "Budapest")
        create_user_and_associated_profile("4meRomance", "coemperor@famemma.net", "John", "Rodriguez", "Berlin")
