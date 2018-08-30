from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import ugettext_lazy as _
from inscription.models import inscription, inscription_slot as inscr_slot, message_history


@user_passes_test(lambda u: u.is_staff)
def inscriptions_view(request):
    total_demanded_places = inscription.get_total_demanded_places()
    total_confirmed_places = inscription.get_total_confirmed_places()
    confirmed_inscriptions = inscription.find_confirmed_inscriptions()
    inscriptions = [{"last_name": inscr.last_name,
                     "first_name": inscr.first_name,
                     "address": inscr.address,
                     "phone": inscr.phone,
                     "number_places": inscr.number_places,
                     "desired_place": inscr.desired_place,
                     "slots": inscr_slot.get_list_slots(inscr),
                     "notifications": _get_notification_icons(inscr)} for inscr in confirmed_inscriptions]
    return render(request, "inscriptions.html", locals())


@user_passes_test(lambda u: u.is_staff)
def inscriptions_summary(request):
    total_confirmed_places = inscription.get_total_confirmed_places()
    inscriptions = inscription.find_confirmed_inscriptions()
    return render(request, "inscriptions_summary.html", locals())


def _get_notification_icons(a_inscription):
    notification_types = inscription.get_notification_types(a_inscription)
    icons = {}
    for type in notification_types:
        if message_history.SUBMISSION_CONFIRMATION == type:
            icons["pencil"] = _('Submission Confirmation')
        elif message_history.INSCRIPTION_CONFIRMATION == type:
            icons["ok"] = _('Inscription Confirmation')
        elif message_history.INSTRUCTIONS == type:
            icons["list-alt"] = _('Instructions')
        elif message_history.WAITING_LIST == type:
            icons["time"] = _('Waiting List')
    return icons
