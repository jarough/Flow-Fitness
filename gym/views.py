from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
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

class EquipmentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Equipment
    fields = "__all__"

    def test_func(self):
        gym = self.get_object()
        return self.request.user == gym.creator

    def valid_form(self, form):
        form.instance.author = self.request.user
        return super().valid_form(form)

class EquipmentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Equipment
    success_url = reverse_lazy('gym-home')

    def test_func(self):
        gym = self.get_object()
        return self.request.user == gym.creator

    
def about(request):
    return render(request, "gym/about.html", {'title': 'About Us | FlowFitness'})