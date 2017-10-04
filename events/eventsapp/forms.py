from django import forms

from .models import Events

class  EventsForm(forms.ModelForm):
	
	class Meta:
		model = Events
		fields = ('title', 'venue', 'text',)
