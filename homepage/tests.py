from django.test import Client
from django.urls import reverse

client = Client()
url = reverse('homepage:index')
response = client.get(url)


def test_homepage_should_respond_status_200_ok():
    assert response.status_code == 200


def test_homepage_response_should_return_title_in_html():
    assert "<title>Holiday Homes</title>" in response.content.decode()
