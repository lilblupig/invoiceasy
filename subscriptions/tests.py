""" Test information for subscription pages """

from django.contrib.auth.models import User
from django.test import TestCase
from.models import StripeCustomer

# Create your tests here.


# Test Models
class TestSubscriptionsModels(TestCase):
    """ Test Subscriptions app model """

    def setUp(self):
        """ Define test form submission data """
        self.test_user = User.objects.create_user(
                            username='profilesuser',
                            email='profiles@email.com',
                            password='testpw'
                        )

        self.stripe_customer = StripeCustomer.objects.create(
                            stripeCustomerId='cus_0123456789',
                            stripeSubscriptionId='sub_0123456789',
                            user_id=self.test_user.id,
                        )

    def test_string_method_returns_name(self):
        """ Check string method returns as expected """
        self.assertEqual(str(self.test_user.username), 'profilesuser')


# Test Views
class TestInvoiceCustomerViews(TestCase):
    """ Test InvoiceCustomer app views """

    def setUp(self):
        """ Define test form submission data """
        self.test_user = User.objects.create_user(
                            username='invoicesuser',
                            email='invoices@email.com',
                            password='testpw'
                        )

    # Test GET responses
    def test_get_subscribe_page(self):
        """ Check subscribe page GET response """
        response = self.client.get('/subscriptions/')
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(login)

    def test_get_success_page(self):
        """ Check success page GET response """
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        response = self.client.get('/subscriptions/success/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(login)
        self.assertTemplateUsed(response, 'subscriptions/success.html')

    def test_get_abort_page(self):
        """ Check abort page GET response """
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        response = self.client.get('/subscriptions/abort/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(login)
        self.assertTemplateUsed(response, 'subscriptions/abort.html')
