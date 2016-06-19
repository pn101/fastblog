from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from users.models import UserProfile

from fastblog.utils import send_sms


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(
                user=instance,
        )
        instance.save()


@receiver(post_save, sender=UserProfile)
def post_save_userprofile(sender, instance, created, **kwargs):
    if instance.is_phonenumber_exists and not instance.signup_sms_sent:
        send_sms(
            sender='01022205736',
            receiver=instance.phonenumber,
            content='Hello {firstname} {lastname}, thank you for signing up.'.format(
                firstname=instance.firstname,
                lastname=instance.lastname,
                ),
        )
        instance.signup_sms_sent = True
        instance.save()
