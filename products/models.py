""" Model information for product and pricing pages """

from django.db import models

# Create your models here.


class Plan(models.Model):
    """ Define data for plans """
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        """ Return name of plan """
        return self.name
