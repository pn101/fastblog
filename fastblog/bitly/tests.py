from django.test import TestCase
from django.contrib.auth.models import User

from bitly.models import BitLink


class BitLinkCreateViewTestCase(TestCase):

    def test_bitlink_create_view_to_return_shorten_hash(self):
        # Create Test User
        test_username = 'username'
        test_password = 'password'
        test_email = 'email'
        test_user = User.objects.create_user(
                username=test_username,
                password=test_password,
                email=test_email,
        )

        # Create Test BitLink
        test_original_url = 'http://google.com'

        test_bitlink = BitLink.objects.create(
                user=test_user,
                original_url=test_original_url,
        )

        # Test for shorten_hash in test_bitlink
        self.assertTrue(
                test_bitlink.shorten_hash,
        )
