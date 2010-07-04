from models import *
from django.contrib.auth.models import User

from forms import *

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse


def render(request,template,context={}):
	return render_to_response(template,context,context_instance=RequestContext(request))


def add_place(request):
	
	if request.method == 'POST':
		form = PlaceForm(request.POST)
		
		if form.is_valid():
			new_place = form.save()
			return HttpResponseRedirect( reverse('activity-page') )
	
	else:
		form = PlaceForm()
		
	return render(request, 'create_place.html', {'form': form})
	
def check_in(request):
	places = Place.objects.all()
	
	if request.method == 'POST':
		POST = request.POST.copy()
		POST['user'] = str(request.user.id)
		
		form = CheckInForm(POST)
		
		if form.is_valid():
			new_check_in = form.save()
			return HttpResponseRedirect( reverse('activity-page') )
	
	else:
		form = CheckInForm(initial={'user': request.user.id})
	
	return render(request, 'check_in.html', {'form': form, 'places': places})