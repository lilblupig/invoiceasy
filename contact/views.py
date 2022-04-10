""" View information for contact page """

from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def contact(request):
    """ View to return contact page """
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
