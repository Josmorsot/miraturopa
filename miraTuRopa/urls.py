from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miraTuRopa.views.home', name='home'),
    # url(r'^miraTuRopa/', include('miraTuRopa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) +static.static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
