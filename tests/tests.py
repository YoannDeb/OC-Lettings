from django.test import Client, SimpleTestCase
from django.urls import reverse


class HomepageSimpleTestCase(SimpleTestCase):

    def test_homepage_should_respond_status_200_ok(self):
        client = Client()
        url = reverse('homepage:index')
        response = client.get(url)
        assert response.status_code == 200

    def test_homepage_response_should_return_title_in_html(self):
        client = Client()
        url = reverse('homepage:index')
        response = client.get(url)
        assert "<title>Holiday Homes</title>" in response.content.decode()
