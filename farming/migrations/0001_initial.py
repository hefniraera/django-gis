# Generated by Django 5.2.2 on 2025-06-08 11:36

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CulinaryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, editable=False, unique=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_update_by', models.TextField()),
                ('name', models.TextField(unique=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacilityMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, editable=False, unique=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_update_by', models.TextField()),
                ('name', models.TextField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CulinarySpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, editable=False, unique=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_update_by', models.TextField()),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('notes', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farming.culinarycategory', to_field='uuid')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, editable=False, unique=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_update_by', models.CharField(max_length=255)),
                ('day_of_week', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('culinary_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farming.culinaryspot', to_field='uuid')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, editable=False, unique=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('last_update_by', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('culinary_spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farming.culinaryspot', to_field='uuid')),
                ('facility_master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farming.facilitymaster', to_field='uuid')),
            ],
            options={
                'unique_together': {('culinary_spot', 'facility_master')},
            },
        ),
    ]
