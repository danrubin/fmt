from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.forms.util import ErrorDict
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, Context, Template
from django.utils.encoding import smart_unicode, force_unicode
from django.utils.http import urlquote
from django.utils.safestring import mark_safe
from django.views.generic import date_based

from forms import ComplaintForm
from models import Complaint


def index(request):
    """
    A wrapper around ``django.views.generic.date_based.archive_index`` that
    will display an entry form for users to input ``Complaint`` objects.
    """
    
    complaints = Complaint.objects.all()
    
    if request.POST:
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ComplaintForm()
    
    return date_based.archive_index(
        request,
        queryset=complaints,
        date_field='published',
        template_name='complaints/complaint_archive.html',
        allow_empty=True,
        extra_context={
            'form': form,
            'total_complaints': len(complaints)
        }
    )