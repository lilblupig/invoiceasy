""" Admin information for subscription pages """

from django.contrib import admin
from .models import StripeCustomer


admin.site.register(StripeCustomer)
