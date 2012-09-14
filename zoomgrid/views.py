# Zoomgrid views
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core import serializers
from django.utils import simplejson
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from zoomgrid.models import Grid


def home(request):
	grid = Grid.objects.select_related('gridcolumn_set', 'gridrow_set', 'gridcell_set').get(pk=1)
	grid_columns = grid.gridcolumn_set.all().order_by("ordinal")
	grid_rows = grid.gridrow_set.all().order_by("ordinal")
	return render_to_response('home.html',
					{ 'grid':grid,
					  'grid_columns':grid_columns,
					  'grid_rows':grid_rows },
					context_instance=RequestContext(request))