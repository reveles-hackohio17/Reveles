from django import forms
from events.models import Event
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class EventForm(forms.ModelForm):
    
    start_time = forms.DateField(widget=DateInput())
    end_time = forms.DateField(widget=DateInput())
    class Meta:
        model = Event
        fields = ('author', 'event_name', 'description', 'start_time', 'end_time', 'address', 'cost', 'image', 'general_category')