from django.conf.urls.defaults import *
from models import *
from views import *

urlpatterns = patterns('location.views',
	url(r'^add_place/$', 'add_place', name='add-place'),
)
