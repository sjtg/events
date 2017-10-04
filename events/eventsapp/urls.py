from django.conf.urls import url 
from . import views 

urlpatterns = [
	url(r'^$', views.events_list, name='events_list'),
	url(r'^events/(?P<pk>\d+)/$', views.events_details, name='events_details'),
	url(r'^events/new/$', views.events_new, name='events_new'),
	url(r'^events/(?P<pk>\d+)/edit/$', views.events_edit, name='events_edit'),
]
