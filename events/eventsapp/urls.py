from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.events_list, name='events_list'),
]