import os
from django.core.mail import send_mail, BadHeaderError
from django.http.response import HttpResponse
from django.template import Context, Template
from inscription.models import message_history as msg_hist


FROM_EMAIL = os.environ.get('EMAIL_FROM', 'brocantebruyeres@gmail.com')


def send_message(recipients, subject, message, type, html_message=None):
    try:
        send_mail(recipient_list=recipients,
                  subject=subject,
                  message=message,
                  from_email=FROM_EMAIL,
                  html_message=html_message)

        str_recipients = ''.join(recipients)
        message_history = msg_hist.MessageHistory(subject=subject, message=message, recipients=str_recipients, type=type)
        message_history.save()
    except BadHeaderError:
        return HttpResponse('Invalid header found.')


def get_subject_from_template(message_template, context=None):
    return _get_from_template(message_template.subject, context)


def get_message_from_template(message_template, context=None):
    return _get_from_template(message_template.message, context)


def _get_from_template(content, context=None):
    template = Template(content)
    if context:
        return template.render(Context(context))
    else:
        return template.render(Context())
