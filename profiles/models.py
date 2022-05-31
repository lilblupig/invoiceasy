""" Model information for profile pages """

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
    """ User detail information """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    business_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50, null=True, blank=True)
    town_or_city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    vat_number = models.CharField(max_length=11, null=True, blank=True)
    bank_account_name = models.CharField(max_length=50, null=True, blank=True)
    bank_account_number = models.CharField(max_length=12, null=True,
                                           blank=True)
    bank_sort_code = models.CharField(max_length=8, null=True, blank=True)
    payment_terms = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        """ Get username """
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create or update a user profile """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
