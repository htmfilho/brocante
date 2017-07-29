from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'address', 'email', 'phone', 'number_places', 'desired_place', 'registered')
    list_filter = ('status',)
    fieldsets = ((None, {'fields': ('last_name', 'first_name', 'status', 'address', 'email', 'phone', 'number_places', 'desired_place')}),)
    search_fields = ['first_name', 'last_name', 'address', 'email', 'phone']


class Inscription(models.Model):
    STATUS_CHOICES = (
        ('NOT_CONFIRMED', _('Not Confirmed')),
        ('CONFIRMED', _('Confirmed')),
        ('WAITING_LIST', _('Waiting List')))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_places = models.IntegerField()
    desired_place = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT_CONFIRMED')
    registered = models.DateTimeField(null=True, auto_now=True)
