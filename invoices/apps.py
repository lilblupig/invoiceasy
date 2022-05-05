""" App config information for invoicing pages """

from django.apps import AppConfig


class InvoicesConfig(AppConfig):
    """ App config for Invoices app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'invoices'
