from django.contrib import admin
from django.db import models
from django.template import loader
from django.utils.translation import ugettext_lazy as _
from inscription.models.inscription import CONFIRMED
from inscription.models import message_history
from inscription.utils import post_officer


class InscriptionSlotAdmin(admin.ModelAdmin):
    list_display = ('inscription', 'slot')
    fieldsets = ((None, {'fields': ('inscription', 'slot')}),)
    raw_id_fields = ('inscription',)
    actions = ['send_instructions']

    def send_instructions(self, request, queryset):
        for record in queryset:
            send_instructions_emails(record.inscription)


class InscriptionSlot(models.Model):
    inscription = models.ForeignKey('Inscription', verbose_name=_("Inscription"))
    slot = models.ForeignKey('Slot', verbose_name=_("Slot"))

    class Meta:
        unique_together = ('inscription', 'slot')

    def __str__(self):
        return "{} - {}".format(self.inscription, self.slot)


def find_by_inscription(inscription):
    return InscriptionSlot.objects.filter(inscription=inscription)


def send_instructions_emails(inscription):
    messages = message_history.find_messages(inscription.email, message_history.INSTRUCTIONS).count()
    if inscription.email and inscription.status == CONFIRMED and messages == 0:
        subject = _('Brocante Bruyères 2017 - Useful Information')
        template = loader.get_template('messages/instructions_fr.eml')
        template_html = loader.get_template('messages/instructions_html_fr.eml')

        inscription_slots = find_by_inscription(inscription)
        slots_quant = inscription_slots.count()
        inscription_slot = inscription_slots.first()

        if slots_quant > 1:
            slots_list = ", ".join([insc_slot.slot.identification for insc_slot in inscription_slots])
            slots = "{}: <strong>{}</strong>".format(_('The numbers of your slots are'), slots_list)
            location = "{}: <strong>{}</strong>".format(_('The location of your slots are'), inscription_slot.slot.location)
        else:
            slots = "{}: <strong>{}<strong>".format(_('The number of your slot is'), inscription_slot.slot.identification)
            location = "{}: <strong>{}<strong>".format(_('The location of your slot is'), inscription_slot.slot.location)

        context = {'slots': slots,
                   'location': location}
        recipients = [inscription.email]
        post_officer.send_message(recipients, subject, template.render(context), message_history.INSTRUCTIONS,
                                  html_message=template_html.render(context))
