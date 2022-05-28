""" Admin information for invoicing pages """

from django.contrib import admin
from .models import InvoiceCustomer, Invoice


class InvoiceCustomerAdmin(admin.ModelAdmin):
    """ Set fields to display in admin """
    list_display = (
        'user',
        'customer_code',
        'customer_first_name',
        'customer_last_name'
    )

    ordering = ('id',)


admin.site.register(InvoiceCustomer, InvoiceCustomerAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    """ Set fields to display in admin """
    list_display = (
        'user',
        'customer_code',
        'invoice_number',
        'invoice_date'
    )

    ordering = ('id',)


admin.site.register(Invoice, InvoiceAdmin)
