""" Forms information for contact page """

from django import forms


class ContactForm(forms.Form):
    """ Form for email contact query """
    first_name = forms.CharField(
        label='First name',
        required=True,
        min_length=2, max_length=50,
    )
    last_name = forms.CharField(
        label='Last name',
        required=True,
        min_length=2, max_length=50,
    )
    email = forms.EmailField(
        label='Email address',
        required=True,
        max_length=150,
    )
    telephone = forms.CharField(
        label='Telephone number',
        required=True,
        min_length=5, max_length=20,
    )
    message = forms.CharField(
        label='Your message',
        required=True,
        widget=forms.Textarea,
        max_length=2000,
    )
