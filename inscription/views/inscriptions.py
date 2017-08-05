from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import ugettext as _

from inscription.models import inscription


@user_passes_test(lambda u: u.is_staff)
def inscriptions_view(request):
    total_demanded_places = inscription.find_total_demanded_places()
    return render(request, "inscriptions.html", locals())
