from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'', include('inscription.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.LoginView.as_view(template_name='login.html'), name='login'),
]

admin.site.site_header = 'Brocante Bruyères'
admin.site.site_title = 'Brocante Bruyères'
admin.site.index_title = 'Brocante Bruyères'
