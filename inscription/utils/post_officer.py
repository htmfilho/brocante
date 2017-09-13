from django.core.mail import send_mail, BadHeaderError
from django.http.response import HttpResponse
from inscription.models import message_history as msg_hist

FROM_EMAIL = "brocante.bruyeres.en.musique@gmail.com"


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