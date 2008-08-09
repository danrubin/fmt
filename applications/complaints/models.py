
from django.db import models
from django.db.models import permalink


class Complaint(models.Model):
    """
    A complaint consists of a user, anonymous or otherwise, writing about
    a specific technology.
    """
    published = models.DateTimeField('Date Published', default=datetime.now)
    complaint = models.TextField()
    name = models.CharField(blank=True, max_length=100)
    technology = models.CharField(max_length=200)
    
    def __unicode__(self):
        return "%s - %s" % (self.name, self.complaint)
    
    @permalink
    def get_absolute_url(self):
        return ('complaint-detail', (), {
            'year'  : self.published.year, 
            'month' : self.published.strftime('%b').lower(), 
            'day'   : self.published.day, 
            'id'    : self.id
        })
    

