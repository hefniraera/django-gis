from django.urls import path
from farming import views
from .views import (
    CulinaryCategoryListView, CulinaryCategoryDetailView,
    CulinaryCategoryCreateView, CulinaryCategoryUpdateView,
    CulinaryCategoryDeleteView, CulinarySpotListView,
    CulinarySpotDetailView, CulinarySpotCreateView,
    CulinarySpotUpdateView, CulinarySpotDeleteView,
)

# URL patterns for the farming app
urlpatterns = [
    # CulinaryCategory URLs
    path('categories/', CulinaryCategoryListView.as_view(), name='culinarycategory-list'),
    path('categories/<uuid:pk>/', CulinaryCategoryDetailView.as_view(), name='culinarycategory-detail'),
    path('categories/add/', CulinaryCategoryCreateView.as_view(), name='culinarycategory-add'),
    path('categories/<uuid:pk>/edit/', CulinaryCategoryUpdateView.as_view(), name='culinarycategory-edit'),
    path('categories/<uuid:pk>/delete/', CulinaryCategoryDeleteView.as_view(), name='culinarycategory-delete'),

    # CulinarySpot URLs
    path('spots/', CulinarySpotListView.as_view(), name='culinaryspot-list'),
    path('spots/<uuid:pk>/', CulinarySpotDetailView.as_view(), name='culinaryspot-detail'),
    path('spots/add/', CulinarySpotCreateView.as_view(), name='culinaryspot-add'),
    path('spots/<uuid:pk>/edit/', CulinarySpotUpdateView.as_view(), name='culinaryspot-edit'),
    path('spots/<uuid:pk>/delete/', CulinarySpotDeleteView.as_view(), name='culinaryspot-delete'),
]
