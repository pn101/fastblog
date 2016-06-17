from django.test import TestCase
from django.contrib.auth.models import User


class UserProfileModelTestCase(TestCase):

    def test_user_to_be_associated_with_user_profile(self):
        test_username = 'username'
        test_password = 'password'
        test_email = 'email'
        test_user = User.objects.create_user(
                username=test_username,
                password=test_password,
                email=test_email,
        )

        self.assertTrue(
                test_user.userprofile,
        )
