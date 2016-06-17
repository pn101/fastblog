from django.test import TestCase


class PricingViewTestCase(TestCase):

    def test_pricing_should_return_200(self):
        response = self.client.get('/pricing/')
        self.assertEqual(
                response.status_code,
                200,
        )
