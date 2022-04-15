""" App config information for profile pages """

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """ App config for Profile app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
