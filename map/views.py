from django.shortcuts import render

# Create your views here.
def main_map(request):
    return render(request, 'map/main_map.html', {})