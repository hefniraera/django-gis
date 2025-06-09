from django.db import models
from django.contrib.gis.db import models
import uuid

class CulinaryCategory(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.TextField()
    name = models.CharField(max_length=255, unique=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Culinary Categories"


class CulinarySpot(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.TextField()
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    geometry = models.PointField(srid=4326)
    category = models.ForeignKey(CulinaryCategory, to_field='uuid', on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Culinary Spots"


class OpeningHours(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.CharField(max_length=255)
    culinary_spot = models.ForeignKey(CulinarySpot, to_field='uuid', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.culinary_spot.name} - {self.day_of_week}"
    
    class Meta:
        verbose_name_plural = "Opening Hours"


class FacilityMaster(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.TextField()
    name = models.TextField(unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Facility Masters"


class Facility(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.TextField()
    culinary_spot = models.ForeignKey(CulinarySpot, to_field='uuid', on_delete=models.CASCADE)
    facility_master = models.ForeignKey(FacilityMaster, to_field='uuid', on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('culinary_spot', 'facility_master')

    def __str__(self):
        return f"{self.culinary_spot.name} - {self.facility_master.name}"
    class Meta:
        verbose_name_plural = "Facilities"


