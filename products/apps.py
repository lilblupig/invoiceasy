""" App config information for product and pricing pages """

from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ App config for Products app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
