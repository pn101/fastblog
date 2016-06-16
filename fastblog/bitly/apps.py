from django.apps import AppConfig


class BitlyConfig(AppConfig):
    name = 'bitly'

    def ready(self):
        from bitly.signals.post_save import post_save_bitlink
