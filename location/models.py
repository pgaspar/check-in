from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
	"""Model representing a physical location"""
	
	name = models.CharField(max_length=100)
	
	geo_lat = models.DecimalField('latitude', max_digits=20, decimal_places=15)
	geo_lon = models.DecimalField('longitude', max_digits=20, decimal_places=15)
	
	def __unicode__(self):
		return u"Place"

class CheckIn(models.Model):
	"""Model representing a Check-In"""
	
	location = models.ForeignKey(Place)
	user = models.ForeignKey(User)
	
	creation_date = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		return u"Check-In"


class Friendship(models.Model):
	"""Model representing a Friendship between two users"""
	
	def __unicode__(self):
		return u"Friendship"

