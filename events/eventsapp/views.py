# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from .models import Events

from .forms import EventsForm

# Create your views here.


#created function  to the events list 

def events_list(request):
	events_posts = Events.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'site/events_list.html', {'events_posts' : events_posts})

def events_details(request, pk):
		events_post = get_object_or_404(Events, pk=pk)
		return render(request, 'site/events_details.html', {'events_post' : events_post})


def events_new(request):
	if request.method == "POST":
           form = EventsForm(request.POST)
       	   if form.is_valid():
             events_post = form.save(commit=False)
             events_post.author = request.user
             events_post.published_date = timezone.now()
             events_post.save()
             return redirect('events_details', pk=events_post.pk)
        else:
            form = EventsForm()
    	return render(request, 'site/events_edit.html', {'form': form})


def events_edit(request, pk):
    events_post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = EventsForm(request.POST, instance=events_post)
        if form.is_valid():
            events_post = form.save(commit=False)
            events_post.author = request.user
            events_post.published_date = timezone.now()
            events_post.save()
            return redirect('events_details', pk=events_post.pk)
    else:
        form = EventsForm(instance=events_post)
    return render(request, 'site/events_edit.html', {'form': form})
