from django.contrib import admin
from django.db import models


class MessageTemplateAdmin(admin.ModelAdmin):
    list_display = ('subject', 'reference')
    fieldsets = ((None, {'fields': ('subject', 'message', 'reference')}),)


class MessageTemplate(models.Model):
    reference = models.CharField(max_length=30, unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()


def get_by_reference(reference):
    messages = MessageTemplate.objects.filter(reference=reference)
    if messages:
        return messages.first()
    else:
        return None
