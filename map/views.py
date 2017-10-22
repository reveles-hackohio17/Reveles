from django.shortcuts import render
from events.models import Event
from django.core import serializers




# Create your views here.
def map(request):
    json_serializer = serializers.get_serializer("json")()
    events = json_serializer.serialize(Event.objects.all(), ensure_ascii=False)
    #events = Event.objects.all()
    return render(request, 'map/map.html', {'events': events})