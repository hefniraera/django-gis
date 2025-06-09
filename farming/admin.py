from django.contrib import admin
from .models import CulinaryCategory, CulinarySpot, OpeningHours, FacilityMaster, Facility

@admin.register(CulinaryCategory)
class CulinaryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_update', 'last_update_by')
    search_fields = ('name',)

@admin.register(CulinarySpot)
class CulinarySpotAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'last_update')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    raw_id_fields = ('category',)
    

@admin.register(OpeningHours)
class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ('culinary_spot', 'day_of_week', 'opening_time', 'closing_time')
    list_filter = ('day_of_week',)
    search_fields = ('culinary_spot__name',)
    raw_id_fields = ('culinary_spot',)

@admin.register(FacilityMaster)
class FacilityMasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_update')
    search_fields = ('name',)

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('culinary_spot', 'facility_master', 'last_update')
    search_fields = ('culinary_spot__name', 'facility_master__name')
    raw_id_fields = ('culinary_spot', 'facility_master')
