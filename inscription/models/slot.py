from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SlotAdmin(admin.ModelAdmin):
    list_display = ('identification', 'location')
    list_filter = ('location',)
    fieldsets = ((None, {'fields': ('location', 'identification')}),)
    ordering = ('identification',)


class Slot(models.Model):
    location = models.ForeignKey('Location', verbose_name=_("Location"), on_delete=models.CASCADE)
    identification = models.CharField(max_length=20, verbose_name=_("Identification"), unique=True)

    def __str__(self):
        return "{} - {}".format(self.identification, self.location)
