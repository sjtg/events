# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from .models import Events


# Create your views here.


#created function  to the events list 

def events_list(request):
	events_posts = Events.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'site/events_list.html', {'events_posts' : events_posts})

def events_details(request, pk):
	events_post = get_object_or_404(Events, pk=pk)
	return render(request, 'site/events_details.html', {'events_post' : events_post})
