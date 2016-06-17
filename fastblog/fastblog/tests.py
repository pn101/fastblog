from django.test import TestCase
from django.core.urlresolvers import reverse


class HomeViewTestCase(TestCase):

    def test_home_view_to_return_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(
                response.status_code,
                200,
        )
