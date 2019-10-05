from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


SUBMISSION_CONFIRMATION = 'SUBMISSION_CONFIRMATION'
INSCRIPTION_CONFIRMATION = 'INSCRIPTION_CONFIRMATION'
WAITING_LIST = 'WAITING_LIST'
INSTRUCTIONS = 'INSTRUCTIONS'
CANCELATION = 'CANCELATION'


TYPE_CHOICES = (
        (SUBMISSION_CONFIRMATION, _('Submission Confirmation')),
        (INSCRIPTION_CONFIRMATION, _('Inscription Confirmation')),
        (WAITING_LIST, _('Waiting List')),
        (INSTRUCTIONS, _('Instructions')),
        (CANCELATION, _('Cancelation')))


class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('recipients', 'subject', 'sent_date', 'type')
    list_filter = ('type',)
    fieldsets = ((None, {'fields': ('recipients', 'subject', 'message', 'type')}),)
    search_fields = ['subject', 'recipients']


class MessageHistory(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    recipients = models.CharField(max_length=100)
    sent_date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, default=INSCRIPTION_CONFIRMATION)


def find_messages(recipient, type=None):
    messages = MessageHistory.objects.filter(recipients=recipient)
    if type:
        messages = messages.filter(type=type)
    return messages.order_by("sent_date")
