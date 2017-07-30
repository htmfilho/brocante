from django.conf.urls import url
from django.contrib import admin
from inscription import views

urlpatterns = [
    url(r'^$', views.inscription, name='inscription'),
    url(r'submission$', views.inscription_submission, name='inscription_submission'),
]
