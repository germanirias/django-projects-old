from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^cms/', include('cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
                 { 'document_root': '/home/gei08a/Projects/tinymce/jscripts/tiny_mce' }),
    (r'^search/$', 'cms.search.views.search'),
    (r'^weblog/', include('coltrane.urls')),
    url(r'', include('django.contrib.flatpages.urls')),
)