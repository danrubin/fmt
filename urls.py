from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page
from django.views.generic import list_detail, date_based
from django.views.generic.simple import direct_to_template, redirect_to
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.syndication.views import feed

from complaints.feeds import LatestComplaints
from complaints.models import Complaint
from complaints.views import index


# Auto-discover `admin.py`
admin.autodiscover()


# Querysets
complaints = {
    'queryset': Complaint.objects.all(),
    'template_object_name': 'complaint',
}


# Feeds
feeds = {
  'complaints': LatestComplaints,
}


# Sitemaps
sitemaps = {
    'complaints': GenericSitemap(complaints, priority=0.8),
}


# URL Patterns
urlpatterns = patterns('',
    
    # Complaints
    url(
        regex   = '^archive/$',
        view    = list_detail.object_list,
        kwargs  = complaints,
        name    = 'archive-index',
    ),
    
    # Homepage
    url(
        regex   = '^$',
        view    = index,
        name    = 'site-home'
    ),
    
    # Feeds
    url(
        regex   = '^feeds/(?P<url>.*)/$',
        view    = feed,
        kwargs  = { 'feed_dict': feeds, },
        name    = 'complaints-feed',
    ),
    
    # Sitemaps
    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    
    # Administration
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/(.*)', admin.site.root),
    
)
