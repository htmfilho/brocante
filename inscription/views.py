import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.utils.translation import ugettext as _

from inscription.forms import InscriptionForm
from inscription.models import inscription as insc
from inscription.utils import post_officer


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(data=request.POST)

        if form.is_valid():
            form.save()

            subject = _('Enrollment Submission Confirmed')
            template = loader.get_template('messages/inscription_submission_confirmation_fr.eml')
            context = {'user': "{} {}".format(form.cleaned_data['first_name'], form.cleaned_data['last_name'])}
            recipients = [form.cleaned_data['email']]
            post_officer.send_message(recipients, subject, template.render(context))

            return HttpResponseRedirect(reverse('inscription_submission'))
        else:
            return render(request, 'inscription.html', locals())
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', locals())


def email_exists(request):
    email = request.GET.get('em')
    user = insc.Inscription.objects.filter(email=email)
    return HttpResponse(json.dumps(True) if user else json.dumps(False), content_type='application/json')


def inscription_submission(request):
    return render(request, 'inscription_submission.html')
