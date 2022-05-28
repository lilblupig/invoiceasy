""" Test information for base public pages """

from django.test import TestCase


class TestHomeViews(TestCase):
    """ Test Contact app views """

    def test_get_home_page(self):
        """ Check home page GET response """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_about_page(self):
        """ Check about page GET response """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')
