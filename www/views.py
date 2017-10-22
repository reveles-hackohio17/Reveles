from django.shortcuts import render
from events.models import Event 
from django.core import serializers

# Create your views here.
def homepage(request):
    return render(request, 'www/index.html', {})

def map(request):
    json_serializer = serializers.get_serializer("json")()
    events = json_serializer.serialize(Event.objects.all(), ensure_ascii=False)
    #events = Event.objects.all()
    return render(request, 'www/map.html', {'events': events})

