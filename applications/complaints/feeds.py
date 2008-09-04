from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.contrib.syndication.feeds import Feed, FeedDoesNotExist

from models import Complaint


# Get the current site.
site = Site.objects.get_current()

class LatestComplaints(Feed):
    """
    A feed of the latest complaints.
    
    """
    title = 'FMT: Recent Complaints'
    link = 'http://%s/' % site.domain
    
    def description(self):
        return 'The latest complaints live from Fuck My Technology.' 
    
    def items(self):
        return Complaint.objects.all()[:50]
    
    def item_link(self):
        return 'http://%s/' % site.domain
