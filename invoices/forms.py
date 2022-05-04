""" Forms information for invoicing pages """

from django import forms
from .models import InvoiceCustomer, Invoice


class InvoiceCustomerForm(forms.ModelForm):
    """ Form for subscriber to add customer """
    class Meta:
        """ Define form fields """
        model = InvoiceCustomer
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_code': 'Choose a code - e.g. "CUST01"',
            'customer_first_name': 'First name/s',
            'customer_last_name': 'Last name',
            'customer_business_name': 'Business name',
            'customer_address_1': 'Address line 1',
            'customer_address_2': 'Address line 2',
            'customer_town_or_city': 'Town or city',
            'customer_county': 'County',
            'customer_postcode': 'Postcode',
            'customer_telephone': 'Telephone number',
            'customer_email': 'Email address',
        }

        self.fields['customer_code'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]


class InvoiceForm(forms.ModelForm):
    """ Form for subscriber to add customer """
    class Meta:
        """ Define form fields """
        model = Invoice
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_code': '',
            'invoice_number': 'This should be sequential',
            'invoice_info': 'Write the invoice details here',
            'invoice_subtotal': '0.00'
        }

        self.fields['customer_code'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[field]
