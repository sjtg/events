# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.utils import timezone

from .models import Events

# Create your views here.


#created function  to the events list 

def events_list(request):
	events_posts = Events.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'site/events_list.html', {'events_posts' : events_posts})
