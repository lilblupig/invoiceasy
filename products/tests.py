""" Test information for product and pricing pages """

from django.test import TestCase
from .models import Plan

# Create your tests here.


# Test Models
class TestProductsModels(TestCase):
    """ Test Products app models """
    def test_string_method_returns_name(self):
        """ Check string method returns as expected """
        plan = Plan.objects.create(
                            name='Test Plan',
                            description='Test products and pricing pages',
                            price=3.00,
                            duration=1,
                            stripe_id='test_stripe_id',
                        )
        self.assertEqual(str(plan), 'Test Plan')


# Test Views
class TestProductsViews(TestCase):
    """ Test Products app views """

    def setUp(self):
        """ Define test product data """
        self.test_product = Plan.objects.create(
                            name='Test Plan',
                            description='Test products and pricing pages',
                            price=3.00,
                            duration=1,
                            stripe_id='test_stripe_id',
                        )

    def test_get_pricing_page(self):
        """ Check pricing GET responses """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/pricing.html')

    def test_get_pricing_detail_page(self):
        """ Check pricing GET responses """
        response = self.client.get('/products/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/plan_detail.html')
