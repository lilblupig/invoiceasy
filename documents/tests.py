""" Test information for PDF creation pages """

from django.contrib.auth.models import User
from subscriptions.models import StripeCustomer
from invoices.models import InvoiceCustomer, Invoice
from django.test import TestCase


class TestDocumentsViews(TestCase):
    """ Test Documents app views """

    def setUp(self):
        """ Define test form submission data """
        self.test_user = User.objects.create_user(
                            username='invoicesuser',
                            email='invoices@email.com',
                            password='testpw'
                        )

        self.test_customer = InvoiceCustomer.objects.create(
                            user_id=self.test_user.id,
                            customer_code='TES002',
                        )

        self.test_invoice = Invoice.objects.create(
                            user_id=self.test_user.id,
                            invoice_number='INV001',
                            invoice_subtotal=100,
                            customer_code_id=self.test_customer.id,
                            invoice_gross=100,
                            invoice_vat=0,
                        )

        self.test_subscription = StripeCustomer.objects.create(
            stripeCustomerId='cus_0123456789',
            stripeSubscriptionId='sub_0123456789',
            user_id=1,
        )

    def test_get_pdf(self):
        """ Check make PDF GET response """
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        response = self.client.get('/documents/1', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'documents/view_pdf.html')
