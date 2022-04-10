""" Forms information for contact page """

from django import forms


class ContactForm(forms.Form):
    """ Form for email contact query """
    first_name = forms.CharField(
        label='First name',
        required=True,
    )
    last_name = forms.CharField(
        label='Last name',
        required=True,
    )
    email = forms.EmailField(
        label='Email address',
        required=True,
    )
    telephone = forms.CharField(
        label='Telephone number',
        required=True,
    )
    subject = forms.CharField(
        label='Subject',
        required=False,
    )
    message = forms.CharField(
        label='Your message',
        required=True,
    )
