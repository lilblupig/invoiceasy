""" View information for contact page """

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from profiles.models import UserProfile
from .forms import ContactForm

# Create your views here.


def contact(request):
    """ View to return contact page """
    # If request is POST get form fields and set as variables
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            web_team = settings.EMAIL_HOST_USER
            subject = 'InvoicEasy contact form submission.'
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']
            message = form.cleaned_data['message']

            # Prepare data for enquiry sent to admin
            enquiry = render_to_string(
                'contact/emails/contact.txt',
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'telephone': telephone,
                    'message': message,
                }
            )

            # Prepare data for auto response sent to user
            response = render_to_string(
                'contact/emails/auto.txt',
                {
                    'first_name': first_name,
                    'message': message,
                }
            )

            # Send both emails and redirect to contact form
            try:
                send_mail(
                    subject,
                    enquiry,
                    email,
                    [web_team]
                )
                send_mail(
                    subject,
                    response,
                    web_team,
                    [email]
                )
                messages.success(request, 'Your message has been sent to the '
                                          'team, we will be in touch shortly.')
            except BadHeaderError:
                messages.error(request, 'We apologise, your message was not '
                                        'sent, please try again later.')
                return HttpResponse('Invalid header found.')
            return redirect('contact')

    # If request is GET, check if user signed in
    if request.user.is_authenticated:
        # If signed in, get user info and populate form
        user_profile = UserProfile.objects.get(user=request.user)
        form = ContactForm(initial={
            'first_name': user_profile.first_name,
            'last_name': user_profile.last_name,
            'email': user_profile.email,
            'telephone': user_profile.telephone,
            })
    else:
        # If not signed in, render blank form
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
