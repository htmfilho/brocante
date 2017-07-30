from django.core.mail import send_mail

FROM_EMAIL = "me@hildeberto.com"


def send_message(recipients, subject, message):
    send_mail(recipient_list=recipients,
              subject=subject,
              message=message,
              from_email=FROM_EMAIL)
