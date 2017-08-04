from django.contrib import admin
from django.db import models
from django.template import loader
from django.utils.translation import ugettext_lazy as _
from inscription.models import message_history
from inscription.utils import post_officer

NOT_CONFIRMED = 'NOT_CONFIRMED'
CONFIRMED = 'CONFIRMED'
WAITING_LIST = 'WAITING_LIST'
CANCELED = 'CANCELED'

STATUS_CHOICES = (
        (NOT_CONFIRMED, _('Not Confirmed')),
        (CONFIRMED, _('Confirmed')),
        (WAITING_LIST, _('Waiting List')),
        (CANCELED, _('Canceled')))


class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'status', 'address', 'email', 'phone', 'number_places', 'desired_place',
                    'registered')
    list_filter = ('status',)
    fieldsets = ((None, {'fields': ('last_name', 'first_name', 'status', 'address', 'email', 'phone', 'number_places',
                                    'desired_place')}),)
    search_fields = ['first_name', 'last_name', 'address', 'email', 'phone']


class Inscription(models.Model):
    first_name = models.CharField(max_length=30, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=30, verbose_name=_("Last Name"))
    address = models.TextField(verbose_name=_("Address"))
    email = models.EmailField(verbose_name=_("Email"), blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))
    number_places = models.IntegerField(verbose_name=_("Places"))
    desired_place = models.TextField(verbose_name=_("Desired Place"), blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=NOT_CONFIRMED, verbose_name=_("Status"))
    registered = models.DateTimeField(null=True, auto_now=True, verbose_name=_("Registered"))

    def save(self, *args, **kwargs):
        send_email_when_confirmed(self)
        super(Inscription, self).save(*args, **kwargs)

    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, self.number_places)


def send_email_when_confirmed(inscription):
    messages = message_history.find_messages(inscription.email, message_history.INSCRIPTION_CONFIRMATION).count()
    if inscription.email and inscription.status == CONFIRMED and messages == 0:
        subject = _('Enrollment Confirmed')
        template = loader.get_template('messages/inscription_confirmation_fr.eml')
        context = {'user': "{} {}".format(inscription.first_name, inscription.last_name),
                   'places': _("1 slot") if inscription.number_places == 1 else _("2 slots")}
        recipients = [inscription.email]
        post_officer.send_message(recipients, subject, template.render(context), message_history.INSCRIPTION_CONFIRMATION)


def find_total_demanded_places():
    sum_number_places = Inscription.objects.exclude(status=CANCELED)\
                                   .exclude(status=WAITING_LIST)\
                                   .aggregate(models.Sum('number_places'))
    if sum_number_places is not None:
        return sum_number_places['number_places__sum']
    else:
        return 0
