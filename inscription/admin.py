from django.contrib import admin
from inscription.models import inscription, message_history

admin.site.register(inscription.Inscription, inscription.InscriptionAdmin)
admin.site.register(message_history.MessageHistory, message_history.MessageHistoryAdmin)
