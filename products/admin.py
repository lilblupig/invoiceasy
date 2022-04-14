""" Admin information for product and pricing pages """

from django.contrib import admin
from .models import Plan

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    """ Set fields to display in admin """
    list_display = (
        'name',
        'price',
    )


admin.site.register(Plan, PlanAdmin)
