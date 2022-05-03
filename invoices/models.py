""" Model information for invoicing pages """

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

# Create your models here.


class InvoiceCustomer(models.Model):
    """ Store Stripe customer info """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_code = models.CharField(max_length=10)
    customer_first_name = models.CharField(max_length=50)
    customer_last_name = models.CharField(max_length=50)
    customer_business_name = models.CharField(max_length=50, null=True, blank=True)
    customer_address_1 = models.CharField(max_length=50)
    customer_address_2 = models.CharField(max_length=50, null=True, blank=True)
    customer_town_or_city = models.CharField(max_length=50)
    customer_county = models.CharField(max_length=50)
    customer_postcode = models.CharField(max_length=50)
    customer_telephone = models.CharField(max_length=50, null=True, blank=True)
    customer_email = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_last_name
