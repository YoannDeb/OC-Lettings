from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


class LettingsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="test_username", password="abc1234", email="test@test.com",
            first_name="test", last_name='test')
        cls.profile = Profile.objects.create(user=cls.user, favorite_city="Madrid")

    def test_user_object(self):
        assert User.objects.get(pk=1).username == "test_username"

    def test_profile_object(self):
        assert Profile.objects.get(pk=1).favorite_city == "Madrid"

    def test_relation_between_letting_and_address_object(self):
        assert Profile.objects.get(pk=1).user == User.objects.get(pk=1)

    def test_lettings_index_should_respond_status_200_ok(self):
        client = Client()
        response = client.get(reverse('profiles:index'))
        assert response.status_code == 200

    def test_lettings_index_response_should_return_title_in_html(self):
        client = Client()
        response = client.get(reverse('profiles:index'))
        assert "<title>Profiles</title>" in response.content.decode()

    def test_lettings_letting_should_respond_status_200_ok(self):
        client = Client()
        response = client.get(reverse('profiles:profile', args=["test_username"]))
        assert response.status_code == 200

    def test_lettings_letting_response_should_return_title_in_html(self):
        client = Client()
        response = client.get(reverse('profiles:profile', args=["test_username"]))
        assert "<title>test_username</title>" in response.content.decode()
