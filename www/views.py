from django.shortcuts import render
from events.model import Event 
# Create your views here.
def homepage(request):
    return render(request, 'www/index.html', {})

def map(request):
	topEvents = Event.objects.order_by('num_attendees')
	return render(request, 'www/map.html', {'topEvents': topEvents})

