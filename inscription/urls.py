from django.conf.urls import url
from django.contrib import admin
from inscription import views

urlpatterns = [
    url(r'^$', views.inscription, name='inscription'),
]
