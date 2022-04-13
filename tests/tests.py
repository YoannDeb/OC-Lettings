from django.test import Client, SimpleTestCase
from django.urls import reverse


class HomepageSimpleTestCase(SimpleTestCase):

    def test_homepage_should_respond_status_200_ok(self):
        """
        Testing that GET request on homepage index page is returning status code 200,
        which means ok.
        """
        client = Client()
        url = reverse('homepage:index')
        response = client.get(url)
        assert response.status_code == 200

    def test_homepage_response_should_return_title_in_html(self):
        """
        Testing that GET request on homepage index page returns html with correct
        title inside.
        """
        client = Client()
        url = reverse('homepage:index')
        response = client.get(url)
        assert "<title>Holiday Homes</title>" in response.content.decode()
