from django.test import Client, TestCase
from django.urls import reverse
from .models import Letting, Address


class LettingsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            number=1, street="rue de Paris", city="TestCity", state="",
            zip_code="75012", country_iso_code="FRA"
        )
        cls.letting = Letting.objects.create(title="Test", address=cls.address)

    def test_letting_object(self):
        assert Letting.objects.get(pk=1).title == "Test"

    def test_address_object(self):
        assert Address.objects.get(pk=1).city == "TestCity"

    def test_relation_between_letting_and_address_object(self):
        assert Letting.objects.get(pk=1).address == Address.objects.get(pk=1)

    def test_lettings_index_should_return_status_200_ok(self):
        client = Client()
        response = client.get(reverse('lettings:index'))
        assert response.status_code == 200

    def test_lettings_index_response_should_return_title_in_html(self):
        client = Client()
        response = client.get(reverse('lettings:index'))
        assert "<title>Lettings</title>" in response.content.decode()

    def test_lettings_letting_should_return_status_200_ok(self):
        client = Client()
        response = client.get(reverse('lettings:letting', args=[1]))
        assert response.status_code == 200

    def test_lettings_letting_response_should_return_title_in_html(self):
        client = Client()
        response = client.get(reverse('lettings:letting', args=[1]))
        assert "<title>Test</title>" in response.content.decode()
