from django.core.mail import send_mail, BadHeaderError
from django.http.response import HttpResponse

FROM_EMAIL = "brocante.bruyeres.en.musique@gmail.com"


def send_message(recipients, subject, message):
    try:
        send_mail(recipient_list=recipients,
                  subject=subject,
                  message=message,
                  from_email=FROM_EMAIL)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')