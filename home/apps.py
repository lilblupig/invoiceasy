""" App config information for base public pages """

from django.apps import AppConfig


class HomeConfig(AppConfig):
    """ App config for Home app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
