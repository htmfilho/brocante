from datetime import date
from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class EditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_inscriptions', 'end_inscriptions', 'start_edition', 'end_edition', 'total_places')
    fieldsets = ((None, {'fields': ('name', 'start_inscriptions', 'end_inscriptions', 'start_edition', 'end_edition', 'total_places', 'invitation')}),)


class Edition(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    start_inscriptions = models.DateField(verbose_name=_("Start of Inscriptions"))
    end_inscriptions = models.DateField(verbose_name=_("End of Inscriptions"))
    start_edition = models.DateField(verbose_name=_("Start of Edition"))
    end_edition = models.DateField(verbose_name=_("End of Edition"))
    invitation = models.TextField(blank=True, null=True)
    total_places = models.IntegerField(blank=True, null=True, verbose_name=_("Number of Places"))

    def __str__(self):
        return self.name


def find_latest_edition():
    return Edition.objects.order_by("-start_inscriptions").first()


def is_inscriptions_period(edition):
    return edition.start_inscriptions <= date.today() <= edition.end_inscriptions


def get_total_places_latest_edition():
    return find_latest_edition().total_places