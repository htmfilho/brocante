from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = ((None, {'fields': ('name',)}),)


class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))

    def __str__(self):
        return self.name