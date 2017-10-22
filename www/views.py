from django.shortcuts import render
from events.models import Event
from django.core import serializers
from .forms import EventForm
from geopy.geocoders import GoogleV3
from django.http import HttpResponseRedirect

# Create your views here.


def homepage(request):
    return render(request, 'www/index.html', {})


def map(request):
    json_serializer = serializers.get_serializer("json")()
    events = json_serializer.serialize(Event.objects.all(), ensure_ascii=False)
    top_posts = Event.objects.order_by('num_likes')
    #events = Event.objects.all()
    return render(request, 'www/map.html', {'events': events, 'top_posts':top_posts})

def add_event(request):

	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			#post.author = request.user
			# try using geopy for address geocoding
			geolocator = GoogleV3(api_key='AIzaSyDTfLfHLouH4c0CndycEPObRyWNwy3Nl8c')
			location = geolocator.geocode(post.address)
			post.latitude = location.latitude
			post.longitude = location.longitude
			post.save()
			return HttpResponseRedirect('/map')
	else:
	    form = EventForm()
	return render(request, 'www/add_event.html', {'form': form})

def event_page(request):
    json_serializer = serializers.get_serializer("json")()
    events = json_serializer.serialize(Event.objects.all(), ensure_ascii=False)
    return render(request, 'www/event_page.html',{'events':events})


