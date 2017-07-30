from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from inscription.forms import InscriptionForm
from brocante.utils import post_officer


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)

        if form.is_valid():
            form.save()

            # subject = _('Enrollment Submission Confirmed')
            # template = loader.get_template('messages/inscription_submission_confirmation_fr.eml')
            # context = {'user': form.cleaned_data['first_name']}
            # recipients = [form.cleaned_data['email']]
            # try:
            #     post_officer.send_message(recipients, subject, template.render(context))
            # except BadHeaderError:
            #     return HttpResponse('Invalid header found.')

            return HttpResponseRedirect(reverse('inscription_submission'))

    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', locals())


def inscription_submission(request):
    return render(request, 'inscription_submission.html')
