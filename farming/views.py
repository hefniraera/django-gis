from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CulinaryCategory, CulinarySpot

# ListView for displaying all CulinaryCategory records
class CulinaryCategoryListView(ListView):
    model = CulinaryCategory
    template_name = 'farming/culinarycategory_list.html'  # Corrected
    context_object_name = 'categories'

# DetailView for displaying details of a single CulinaryCategory
class CulinaryCategoryDetailView(DetailView):
    model = CulinaryCategory
    template_name = 'farming/culinarycategory_detail.html'  # Corrected

# CreateView for adding a new CulinaryCategory
class CulinaryCategoryCreateView(CreateView):
    model = CulinaryCategory
    fields = ['name', 'notes', 'last_update_by']
    template_name = 'farming/culinarycategory_form.html'  # Corrected
    success_url = reverse_lazy('culinarycategory-list')

# UpdateView for editing an existing CulinaryCategory
class CulinaryCategoryUpdateView(UpdateView):
    model = CulinaryCategory
    fields = ['name', 'notes', 'last_update_by']
    template_name = 'farming/culinarycategory_form.html'  # Corrected
    success_url = reverse_lazy('culinarycategory-list')

# DeleteView for deleting a CulinaryCategory
class CulinaryCategoryDeleteView(DeleteView):
    model = CulinaryCategory
    template_name = 'farming/culinarycategory_confirm_delete.html'  # Corrected
    success_url = reverse_lazy('culinarycategory-list')


# ListView for displaying all CulinarySpot records
class CulinarySpotListView(ListView):
    model = CulinarySpot
    template_name = 'templates/farming/culinaryspot_list.html'
    context_object_name = 'spots'

# DetailView for displaying details of a single CulinarySpot
class CulinarySpotDetailView(DetailView):
    model = CulinarySpot
    template_name = 'templates/farming/culinaryspot_detail.html'

# CreateView for adding a new CulinarySpot
class CulinarySpotCreateView(CreateView):
    model = CulinarySpot
    fields = ['name', 'description', 'geometry', 'category', 'notes', 'last_update_by']
    template_name = 'templates/farming/culinaryspot_form.html'
    success_url = reverse_lazy('culinaryspot-list')

# UpdateView for editing an existing CulinarySpot
class CulinarySpotUpdateView(UpdateView):
    model = CulinarySpot
    fields = ['name', 'description', 'geometry', 'category', 'notes', 'last_update_by']
    template_name = 'templates/farming/culinaryspot_form.html'
    success_url = reverse_lazy('culinaryspot-list')

# DeleteView for deleting a CulinarySpot
class CulinarySpotDeleteView(DeleteView):
    model = CulinarySpot
    template_name = 'templates/farming/culinaryspot_confirm_delete.html'
    success_url = reverse_lazy('culinaryspot-list')



