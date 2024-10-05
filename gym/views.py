from django.shortcuts import render, HttpResponse
from . import models

equipment = [
    {
        'id': '22102',
        'name': 'Rowing Machine',
        'price': '£100'
    },
    {
        'id': '22103',
        'name': 'Weights',
        'price': '£20'
    },
    {
        'id': '22104',
        'name': 'Skipping Ropes',
        'price': '£10'
    }
]

# Create your views here.
def home(request):
    equipment = models.Equipment.objects.all()
    context = {
        'equipment': equipment
    }
    return render(request, "gym/home.html", context)

def about(request):
    return render(request, "gym/about.html", {'title': 'About Us | FlowFitness'})