from django.conf.urls import url
from inscription.views import inscription_form, inscriptions

urlpatterns = [
    url(r'^$', inscription_form.inscription, name='inscription'),
    url(r'^email$', inscription_form.email_exists, name='email_exists'),
    url(r'submission$', inscription_form.inscription_submission, name='inscription_submission'),
    url(r'inscriptions$', inscriptions.inscriptions_view, name='inscriptions')
]
