import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from inscription.forms import InscriptionForm
from inscription.models import inscription as insc


def inscription(request):
    total_places_reached = insc.is_total_places_reached()
    if request.method == 'POST':
        form = InscriptionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('inscription_submission'))
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', locals())


def email_exists(request):
    email = request.GET.get('em')
    user = insc.Inscription.objects.filter(email=email)
    return HttpResponse(json.dumps(True) if user else json.dumps(False), content_type='application/json')


def inscription_submission(request):
    return render(request, 'inscription_submission.html')
