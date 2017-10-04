# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


#created function  to the events list 

def events_list(request):
	return render(request, 'site/events_list.html', {})
