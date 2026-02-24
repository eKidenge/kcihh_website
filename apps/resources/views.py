from django.shortcuts import render, get_object_or_404
from .models import Resource

def resources(request):
    resources_list = Resource.objects.all().order_by('-published_date')
    return render(request, 'resources/index.html', {'resources': resources_list})

def resource_detail(request, slug):
    resource = get_object_or_404(Resource, slug=slug)
    return render(request, 'resources/detail.html', {'resource': resource})