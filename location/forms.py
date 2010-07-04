from django.forms import ModelForm
from django import forms
from models import *


class PlaceForm(ModelForm):
	geo_lat = forms.DecimalField('latitude', max_digits=20, decimal_places=15, widget=forms.HiddenInput)
	geo_lon = forms.DecimalField('longitude', max_digits=20, decimal_places=15, widget=forms.HiddenInput)
	
	class Meta:
		model = Place

class CheckInForm(ModelForm):
	
	location = forms.ModelChoiceField(Place, widget=forms.HiddenInput)
	
	class Meta:
		model = CheckIn
		exclude = ('user',)