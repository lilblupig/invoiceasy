""" Test information for Profile pages """

from django.contrib.auth.models import User
from django.test import TestCase
from .forms import UserProfileForm
from .models import UserProfile

# Create your tests here.


# Test Forms
class TestUserProfilesForm(TestCase):
    """ Check form fields behave as expected """
    def test_first_name_is_required(self):
        """ Check required fields are treated correctly """
        form = UserProfileForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')

    def test_telephone_field_is_not_required(self):
        """ Check optional fields are treated correctly """
        form = UserProfileForm({'telephone': ''})
        self.assertTrue(form.is_valid)


# Test Models
class TestProfilesModels(TestCase):
    """ Test Profiles app models """

    def setUp(self):
        """ Define test form submission data """
        self.test_user = User.objects.create_user(
                            username='profilesuser',
                            email='profiles@email.com',
                            password='testpw'
                        )

        self.user_profile = UserProfile.objects.update(
                            first_name='Profiles Name',
                            last_name='Profiles Surname',
                            email='profiles@email.com',
                            telephone='01234 567890',
                        )

    def test_string_method_returns_name(self):
        """ Check string method returns as expected """
        self.assertEqual(str(self.test_user.username), 'profilesuser')


# Test Views
class TestProfilesViews(TestCase):
    """ Test Profiles app views """

    def setUp(self):
        """ Define test form submission data """
        self.test_user = User.objects.create_user(
                            username='profilesuser',
                            email='profiles@email.com',
                            password='testpw'
                        )

        self.user_profile = UserProfile.objects.update(
                            first_name='Profiles Name',
                            last_name='Profiles Surname',
                            email='profiles@email.com',
                            telephone='01234 567890',
                        )

    def test_get_profile_form(self):
        """ Check profiles GET responses """
        response = self.client.get('/profiles/')
        login = self.client.login(username=self.test_user.username,
                                  password='testpw')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(login)

    def test_post_profile_form(self):
        """ Check profiles POST responses """
        # Define test form submission data
        test_form = {
            'first_name': 'Profile Name',
            'last_name': 'Profile Surname',
            'business_name': 'Profile Business',
            'address_1': '1 Test Profile',
            'town_or_city': 'Profile Town',
            'county': 'Profile County',
            'postcode': 'PO5 6ST',
        }
        response = self.client.post('/profiles/', test_form)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user_profile, 1)
