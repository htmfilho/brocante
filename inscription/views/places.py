from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from inscription.models import inscription_slot as inscr_slot


@user_passes_test(lambda u: u.is_staff)
def places_view(request):
    available_slots = inscr_slot.find_available_slots()
    return render(request, "places.html", locals())
