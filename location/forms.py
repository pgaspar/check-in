from django.forms import ModelForm
from django import forms
from models import *


class PlaceForm(ModelForm):
	geo_lat = forms.DecimalField('latitude', max_digits=20, decimal_places=15, widget=forms.HiddenInput)
	geo_lon = forms.DecimalField('longitude', max_digits=20, decimal_places=15, widget=forms.HiddenInput)
	
	class Meta:
		model = Place

class CheckInForm(ModelForm):
	
	user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
	location = forms.ModelChoiceField(queryset=Place.objects.all(), widget=forms.HiddenInput)
	
	class Meta:
		model = CheckIn