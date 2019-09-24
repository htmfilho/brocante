from django.contrib import admin
from django.db import models
from django.template import loader
from django.utils.translation import ugettext_lazy as _
from inscription.models.inscription import CONFIRMED
from inscription.models import message_history, message_template, slot
from inscription.utils import post_officer


class InscriptionSlotAdmin(admin.ModelAdmin):
    list_display = ('slot', 'inscription')
    list_filter = ('slot__location',)
    fieldsets = ((None, {'fields': ('inscription', 'slot')}),)
    raw_id_fields = ('inscription',)
    actions = ['send_instructions']
    search_fields = ['slot__identification', 'inscription__first_name', 'inscription__last_name']

    def send_instructions(self, request, queryset):
        for record in queryset:
            send_instructions_emails(record.inscription)


class InscriptionSlot(models.Model):
    inscription = models.ForeignKey('Inscription', verbose_name=_("Inscription"), on_delete=models.CASCADE)
    slot = models.OneToOneField('Slot', verbose_name=_("Slot"), on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.slot, self.inscription)


def find_by_inscription(inscription):
    return InscriptionSlot.objects.filter(inscription=inscription)


def send_instructions_emails(inscription):
    messages = message_history.find_messages(inscription.email, type=message_history.INSTRUCTIONS).count()
    if inscription.email and inscription.status == CONFIRMED and messages == 0:
        msg_template = message_template.get_by_reference(message_history.INSTRUCTIONS)
        if msg_template:
            subject = post_officer.get_subject_from_template(msg_template)
            
            inscription_slots = find_by_inscription(inscription)
            num_slots = inscription_slots.count()
            inscription_slot = inscription_slots.first()

            if num_slots > 1:
                slots_list = _get_list_slots(inscription_slots)
                slots_label = _('The numbers of your slots are')
                slots = slots_list
                location_label = _('The location of your slots are')
                location = inscription_slot.slot.location
            else:
                slots_label = _('The number of your slot is')
                slots = inscription_slot.slot.identification
                location_label = _('The location of your slot is')
                location = inscription_slot.slot.location

            context = {'slots_label': slots_label,
                    'slots': slots,
                    'location_label': location_label,
                    'location': location}
            message = post_officer.get_message_from_template(msg_template, context)
            recipients = [inscription.email]
            post_officer.send_message(recipients, subject, message, message_history.INSTRUCTIONS)


def _get_list_slots(inscription_slots):
    return ", ".join([insc_slot.slot.identification for insc_slot in inscription_slots])


def get_list_slots(inscription):
    inscription_slots = find_by_inscription(inscription)
    return _get_list_slots(inscription_slots)


def find_available_slots():
    return slot.Slot.objects.exclude(id__in=InscriptionSlot.objects.values("slot"))
