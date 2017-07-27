from django.contrib import admin
from inscription import models

admin.site.register(models.Inscription, models.InscriptionAdmin)
