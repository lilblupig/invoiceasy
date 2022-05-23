""" Test information for invoicing pages """

from django.contrib.auth.models import User
from django.test import TestCase
from subscriptions.models import StripeCustomer
from .forms import InvoiceCustomerForm
from .models import InvoiceCustomer, Invoice

# Create your tests here.


# Test Forms
class TestInvoiceCustomerForm(TestCase):
    """ Check form fields behave as expected """
    def test_first_name_is_required(self):
        """ Check required fields are treated correctly """
        form = InvoiceCustomerForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('customer_first_name', form.errors.keys())
        self.assertEqual(
            form.errors['customer_first_name'][0], 'This field is required.')

    def test_telephone_field_is_not_required(self):
        """ Check optional fields are treated correctly """
        form = InvoiceCustomerForm({'customer_telephone': ''})
        self.assertTrue(form.is_valid)


# Test Models
class TestInvoiceCustomerModels(TestCase):
    """ Test InvoiceCustomer app models """

    def setUp(self):
        """ Define test form submission data """
        self.test_user = User.objects.create_user(
                            username='invoicesuser',
                            email='invoices@email.com',
                            password='testpw'
                        )

        self.test_customer = InvoiceCustomer.objects.create(
                            user_id=1,
                            customer_code='TES002',
                        )

    def test_string_method_returns_customer_code(self):
        """ Check string method returns as expected """
        invoice_customer = InvoiceCustomer.objects.create(
                            user_id=1,
                            customer_code='TES001',
                        )
        self.assertEqual(str(invoice_customer), 'TES001')

    def test_string_method_returns_invoice_number(self):
        """ Check string method returns as expected """
        invoice = Invoice.objects.create(
                            user_id=1,
                            invoice_number='INV001',
                            invoice_subtotal=100,
                            customer_code_id=1,
                            invoice_gross=100,
                            invoice_vat=0,
                        )
        self.assertEqual(str(invoice), 'INV001')


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

        self.test_customer = InvoiceCustomer.objects.create(
                            user_id=1,
                            customer_code='TES002',
                        )

        self.test_invoice = Invoice.objects.create(
                            user_id=1,
                            invoice_number='INV001',
                            invoice_subtotal=100,
                            customer_code_id=1,
                            invoice_gross=100,
                            invoice_vat=0,
                        )

        self.test_subscription = StripeCustomer.objects.create(
            stripeCustomerId='cus_0123456789',
            stripeSubscriptionId='sub_0123456789',
            user_id=1,
        )

    # Test GET responses
    def test_get_dashboard_page(self):
        """ Check dashboard page GET response """
        response = self.client.get('/invoices/')
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(login)

    def test_get_invoice_customer_form(self):
        """ Check customer form GET response """
        response = self.client.get('/invoices/customer/1')
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(login)

    def test_get_invoice_form(self):
        """ Check invoice form GET response """
        response = self.client.get('/invoices/invoice/1')
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(login)

    def test_get_delete_customer(self):
        """ Check delete customer GET response """
        response = self.client.get('/invoices/delete_customer/1')
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(login)

    def test_get_delete_invoice(self):
        """ Check delete invoice GET response """
        response = self.client.get('/invoices/delete_invoice/1')
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(login)

    # Test POST responses
    def test_post_invoice_customer_form(self):
        """ Check customer form POST response """
        # Ensure user is logged in
        self.client.force_login(self.test_user)
        # Create customer instance in DB
        test_customer = InvoiceCustomer.objects.create(
            user_id=self.test_user.id,
            customer_code='TES003',
            customer_first_name='Customer Name',
            customer_last_name='Customer Surname',
            customer_address_1='1 Test Customer',
            customer_town_or_city='Customer Town',
            customer_county='Customer County',
            customer_postcode='PO5 6ST',
            customer_email='customer@email.com',
        )
        # Create POST
        response = self.client.post(f'/invoices/customer/{test_customer.id}', {
            'user_id': self.test_user.id,
            'customer_code': 'TES003',
            'customer_first_name': 'Updated Name',
            'customer_last_name': 'Customer Surname',
            'customer_address_1': '1 Test Customer',
            'customer_town_or_city': 'Customer Town',
            'customer_county': 'Customer County',
            'customer_postcode': 'PO5 6ST',
            'customer_email': 'customer@email.com',
        })
        # Check updated information is as expected
        updated_customer = InvoiceCustomer.objects.get(id=test_customer.id)
        self.assertEqual(updated_customer.customer_first_name, 'Updated Name')
        self.assertEqual(response.status_code, 200)

    def test_post_invoice_form(self):
        """ Check customer form POST response """
        # Ensure user is logged in
        self.client.force_login(self.test_user)
        # Create invoice instance in DB
        test_invoice = Invoice.objects.create(
            user_id=self.test_user.id,
            customer_code_id=self.test_customer.id,
            invoice_number='INV002',
            invoice_info='Bloopy bloop',
            invoice_subtotal=100.00,
            invoice_date='01/01/2022',
            invoice_gross=100.00,
            invoice_vat=0.00,
        )

        # Create POST
        response = self.client.post(f'/invoices/invoice/{test_invoice.id}', {
            'customer_code_id': self.test_customer.id,
            'invoice_number': 'INV002',
            'invoice_info': 'Doopy doop',
        })
        self.assertEqual(response.status_code, 200)
