from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class HomeViewTestCase(TestCase):

    def test_home_view_to_return_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(
                response.status_code,
                200,
        )


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
