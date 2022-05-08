""" App config information for for PDF creation pages """

from django.apps import AppConfig


class DocumentsConfig(AppConfig):
    """ App config for for PDF creation app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'documents'
