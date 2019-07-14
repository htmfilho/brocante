from django.conf.urls import url
from website.views import home

urlpatterns = [
    url(r'^$', home.homepage, name='homepage'),
]
