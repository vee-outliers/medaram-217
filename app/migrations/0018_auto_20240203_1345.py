# Generated by Django 3.2.5 on 2024-02-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_outdepotvehiclesentback'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicledetails',
            name='depot_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='vehicledetails',
            name='region_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='vehicledetails',
            name='zone_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='outdepotvehiclesentback',
            name='unique_no_bus_no',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
