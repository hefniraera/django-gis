from django.contrib import admin
from .models import (
    PropertyType,
    Province,
    Organisation,
    Property,
    TaxonRank,
    Taxon,
    AnnualPopulation
)

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_code', 'province', 'property_type', 'organisation')
    search_fields = ('name', 'short_code')
    list_filter = ('province', 'property_type', 'organisation')

@admin.register(Taxon)
class TaxonAdmin(admin.ModelAdmin):
    list_display = ('scientific_name', 'taxon_rank', 'parent')
    search_fields = ('scientific_name', 'common_name_varbatim')

@admin.register(AnnualPopulation)
class AnnualPopulationAdmin(admin.ModelAdmin):
    list_display = ('property', 'year', 'total', 'area_available_to_species')
    search_fields = ('property__name', 'year')
    list_filter = ('year',)