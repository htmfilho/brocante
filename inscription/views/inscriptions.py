from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from inscription.models import inscription


@user_passes_test(lambda u: u.is_staff)
def inscriptions_view(request):
    total_demanded_places = inscription.get_total_demanded_places()
    total_confirmed_places = inscription.get_total_confirmed_places()
    inscriptions = inscription.find_all()
    return render(request, "inscriptions.html", locals())
