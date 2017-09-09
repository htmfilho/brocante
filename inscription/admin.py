from django.contrib import admin
from inscription.models import inscription, inscription_slot, location, message_history, slot

admin.site.register(inscription.Inscription, inscription.InscriptionAdmin)
admin.site.register(inscription_slot.InscriptionSlot, inscription_slot.InscriptionSlotAdmin)
admin.site.register(location.Location, location.LocationAdmin)
admin.site.register(message_history.MessageHistory, message_history.MessageHistoryAdmin)
admin.site.register(slot.Slot, slot.SlotAdmin)