""" Forms information for profile pages """

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Form for email contact query """
    class Meta:
        """ Define form fields """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First name/s',
            'last_name': 'Last name',
            'business_name': 'Business name',
            'address_1': 'Address line 1',
            'address_2': 'Address line 2',
            'town_or_city': 'Town or city',
            'county': 'County',
            'postcode': 'Postcode',
            'telephone': 'Telephone number',
            'email': 'Email address',
            'vat_number': 'VAT number (if applicable)',
            'bank_account_name': 'Bank account name',
            'bank_account_number': 'Bank account number',
            'bank_sort_code': 'Bank sort code',
            'payment_terms': 'Payment terms',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = placeholders[
                                                                field
                                                            ]
