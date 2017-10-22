from django.shortcuts import render
from events.models import Event 
from django.core import serializers
from .forms	import EventForm

# Create your views here.
def homepage(request):
    return render(request, 'www/index.html', {})

def map(request):
    json_serializer = serializers.get_serializer("json")()
    events = json_serializer.serialize(Event.objects.all(), ensure_ascii=False)
    #events = Event.objects.all()
    return render(request, 'www/map.html', {'events': events})

def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
			#try using geopy for address geocoding
            #return redirect('map')
    else:
        form = EventForm()
    return render(request, 'www/add_event.html', {'form': form})

def event_page(request):
    json_serializer = serializers.get_serializer("json")()
    events = json_serializer.serialize(Event.objects.all(), ensure_ascii=False)
    return render(request, 'www/event_page.html',{'events':events})



