""" Test information for Contact page """

from django.test import TestCase
from .forms import ContactForm

# Create your tests here.


class TestContactForm(TestCase):
    """ Check form fields behave as expected """
    def test_first_name_is_required(self):
        """ Check required fields are treated correctly """
        form = ContactForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')

    def test_telephone_field_is_not_required(self):
        """ Check optional fields are treated correctly """
        form = ContactForm({'telephone': ''})
        self.assertTrue(form.is_valid)


class TestContactViews(TestCase):
    """ Test Contact app views """

    def test_get_contact_form(self):
        """ Check contact GET responses """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_post_contact_form(self):
        """ Check contact POST responses (302 as redirects on POST) """
        # Define test form submission data
        test_form = {
            'first_name': 'Contact Name',
            'last_name': 'Contact Surname',
            'email': 'contact@email.com',
            'telephone': '01234 567890',
            'message': 'Test Contact submission',
        }
        response = self.client.post('/contact/', test_form)
        self.assertRedirects(response, '/contact/')
        self.assertEqual(response.status_code, 302)
