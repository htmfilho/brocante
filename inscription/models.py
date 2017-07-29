from django.db import models
from django.contrib import admin

class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'email', 'phone', 'number_places', 'desired_place')
    fieldsets = ((None, {'fields': ('last_name', 'first_name', 'address', 'email', 'phone', 'number_places', 'desired_place')}),)
    search_fields = ['first_name', 'last_name', 'address', 'email', 'phone']
    

class Inscription(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    number_places = models.IntegerField()
    desired_place = models.TextField()
