from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class InscriptionSlotAdmin(admin.ModelAdmin):
    list_display = ('inscription', 'slot')
    fieldsets = ((None, {'fields': ('inscription', 'slot')}),)


class InscriptionSlot(models.Model):
    inscription = models.ForeignKey('Inscription', verbose_name=_("Inscription"))
    slot = models.ForeignKey('Slot', verbose_name=_("Slot"))

    class Meta:
        unique_together = ('inscription', 'slot')
