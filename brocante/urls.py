from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('inscription.urls')),
]

admin.site.site_header = 'Brocante Bruyères'
admin.site.site_title = 'Brocante Bruyères'
admin.site.index_title = 'Brocante Bruyères'
