from django.db import models

# Create your models here.

class Place(models.Model):
	"""Model representing a physical location"""

	def __unicode__(self):
		return u"Place"

class CheckIn(models.Model):
	"""Model representing a Check-In"""

	def __unicode__(self):
		return u"Check-In"
