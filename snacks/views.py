from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack


class SnackListView(ListView):
    template_name='snacks_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name="snacks_detail.html"
    model= Snack

class SnackCreateView(CreateView):
    template_name="snacks_create.html"
    model= Snack
    fields=['title', 'description', 'purchaser']

class SnackUpdateView(UpdateView):
    template_name="snacks_update.html"
    model= Snack
    fields=['title', 'description', 'purchaser']

class SnackDeleteView(DeleteView):
    template_name='snacks_delete.html'
    model= Snack
    success_url=reverse_lazy('snacks_list')