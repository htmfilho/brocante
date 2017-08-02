from django.contrib import admin
from django.db import models


class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ('recipients', 'subject', 'sent_date')
    fieldsets = ((None, {'fields': ('recipients', 'subject', 'message')}),)
    search_fields = ['subject', 'content', 'inscription']


class MessageHistory(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    recipients = models.CharField(max_length=100)
    sent_date = models.DateTimeField(auto_now=True)
