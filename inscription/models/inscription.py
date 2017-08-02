from django.contrib import admin
from django.db import models
from django.template import loader
from django.utils.translation import ugettext_lazy as _

from inscription.utils import post_officer


class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'address', 'email', 'phone', 'number_places', 'desired_place',
                    'registered')
    list_filter = ('status',)
    fieldsets = ((None, {'fields': ('last_name', 'first_name', 'status', 'address', 'email', 'phone', 'number_places',
                                    'desired_place')}),)
    search_fields = ['first_name', 'last_name', 'address', 'email', 'phone']


class Inscription(models.Model):
    STATUS_CHOICES = (
        ('NOT_CONFIRMED', _('Not Confirmed')),
        ('CONFIRMED', _('Confirmed')),
        ('WAITING_LIST', _('Waiting List')),
        ('CANCELED', _('Canceled')))

    first_name = models.CharField(max_length=30, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=30, verbose_name=_("Last Name"))
    address = models.TextField(verbose_name=_("Address"))
    email = models.EmailField(verbose_name=_("Email"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))
    number_places = models.IntegerField(verbose_name=_("Places"))
    desired_place = models.TextField(verbose_name=_("Desired Place"), blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NOT_CONFIRMED', verbose_name=_("Status"))
    registered = models.DateTimeField(null=True, auto_now=True, verbose_name=_("Registered"))

    def save(self, *args, **kwargs):
        if self.status == 'CONFIRMED':
            subject = _('Enrollment Confirmed')
            template = loader.get_template('messages/inscription_confirmation_fr.eml')
            context = {'user': "{} {}".format(self.first_name, self.last_name),
                       'places': _("1 slot") if self.number_places == 1 else _("2 slots")}
            recipients = [self.email]
            post_officer.send_message(recipients, subject, template.render(context))

        super(Inscription, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, self.number_places)
