from django.shortcuts import render
from inscription.models import edition


def homepage(request):
    latest_edition = edition.find_latest_edition()
    is_inscriptions_period = edition.is_inscriptions_period(latest_edition)
    return render(request, 'homepage.html', locals())
