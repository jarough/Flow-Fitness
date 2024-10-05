from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models

# Create your views here.
def home(request):
    equipment = models.Equipment.objects.all()
    context = {
        'equipment': equipment
    }
    return render(request, "gym/home.html", context)

class EquipmentListView(ListView):
    model = models.Equipment
    template_name = 'gym/home.html'
    context_object_name = 'equipment'


class EquipmentDetailView(DetailView):
    model = models.Equipment


class EquipmentCreateView(LoginRequiredMixin, CreateView):
    model = models.Equipment
    fields = "__all__"

    def valid_form(self, form):
        form.instance.author = self.request.user
        return super().valid_form(form)

class EquipmentUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Equipment
    fields = "__all__"

    def valid_form(self, form):
        form.instance.author = self.request.user
        return super().valid_form(form)

def about(request):
    return render(request, "gym/about.html", {'title': 'About Us | FlowFitness'})