""" View information for contact page """

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from .forms import ContactForm

# Create your views here.


def contact(request):
    """ View to return contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'InvoicEasy contact form submission.',
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'telephone': form.cleaned_data['telephone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL]
                )
                messages.success(request, 'Your message has been sent to the '
                                          'team, we will be in touch shortly.')
            except BadHeaderError:
                messages.error(request, 'We apologise, your message was not '
                                        'sent, please try again later.')
                return HttpResponse('Invalid header found.')
            return redirect('contact')

    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
