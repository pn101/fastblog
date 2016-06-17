from django.test import TestCase

class PricingViewTestCase(TestCase):
    def setUp(self):
        self.response = self.client.get('/pricing/')

    def test_pricing_should_return_200(self):
        self.assertEqual(
                self.response.status_code,
                200,
        )
