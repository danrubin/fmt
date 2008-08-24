from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page
from django.views.generic import list_detail, date_based
from django.views.generic.simple import direct_to_template, redirect_to
from django.contrib.sitemaps import GenericSitemap
from django.contrib import admin

from complaints.models import Complaint


# Auto-discover `admin.py`
admin.autodiscover()

# Querysets
complaints = {
    'queryset': Complaint.objects.all(),
    'date_field': 'published',
    'template_object_name': 'complaint',
    'num_latest': 20,
}


# Sitemaps
sitemaps = {
#    'complaints': GenericSitemap(complaints_sitemap, priority=0.8),
}


# URL Patterns
urlpatterns = patterns('',
    
    # Complaints
    url(
        regex   = '^archive/$',
        view    = date_based.archive_index,
        kwargs  = complaints,
        name    = 'archive-index',
    ),
    
    # Homepage
    url(r'^$', direct_to_template, { 'template': 'home.html' }, name='site-home'),
    
    # Sitemaps
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    
    # Administration
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/var/www/fmt/static', 'show_indexes': True}),
    )