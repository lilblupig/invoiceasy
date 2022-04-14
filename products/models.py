""" Model information for product and pricing pages """

from django.db import models

# Create your models here.


class Plan(models.Model):
    """ Define data for plans """
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def get_name(self):
        """ Return name of plan """
        return self.name
