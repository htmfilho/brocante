from django.conf.urls import url
from django.contrib import admin
from inscription import views

urlpatterns = [
    url(r'^$', views.inscription, name='inscription'),
    url(r'^email$', views.email_exists, name='email_exists'),
    url(r'submission$', views.inscription_submission, name='inscription_submission'),
]
