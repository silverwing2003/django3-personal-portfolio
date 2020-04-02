from django.shortcuts import render
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all()  #database project objects
    return render(request, 'portfolio/home.html', {'projects':projects})
