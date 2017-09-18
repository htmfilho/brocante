from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from inscription.models import inscription, inscription_slot as inscr_slot


@user_passes_test(lambda u: u.is_staff)
def inscriptions_view(request):
    total_demanded_places = inscription.get_total_demanded_places()
    total_confirmed_places = inscription.get_total_confirmed_places()
    inscriptions = [{"last_name": inscr.last_name,
                     "first_name": inscr.first_name,
                     "address": inscr.address,
                     "phone": inscr.phone,
                     "number_places": inscr.number_places,
                     "desired_place": inscr.desired_place,
                     "slots": inscr_slot.get_list_slots(inscr)} for inscr in inscription.find_confirmed_inscriptions()]
    return render(request, "inscriptions.html", locals())
