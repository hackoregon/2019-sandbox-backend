# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.gis.db.models.fields import GeometryField


class AllSweepsV02(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    reportdate = models.TextField(blank=True, null=True)
    cleantype = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    maintenanceproject = models.TextField(blank=True, null=True)
    green_space = models.TextField(db_column='green.space', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    excessive_heat_cold = models.TextField(db_column='excessive.heat.cold', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    estimated_geocode = models.TextField(db_column='estimated.geocode', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    polygon_as_point_field = models.TextField(db_column='polygon.as.point?', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    notes = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    accuracy = models.TextField(blank=True, null=True)
    checked_aurelia_2018_09_2018_11_field = models.TextField(db_column='checked_aurelia(2018_09/2018_11)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flag_alex = models.FloatField(blank=True, null=True)
    row_num_alex = models.FloatField(blank=True, null=True)
    still_need_checked_y_n_dan = models.TextField(db_column='still need checked (y/n)_dan', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    changed_y_n_dan = models.TextField(db_column='changed(y/n)_dan', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    repeats_not_matching_dan = models.FloatField(db_column='repeats not matching?_dan', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    wkb_geometry = GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_sweeps_v02'


class RlisNeighborhoods(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    sum_area = models.FloatField(blank=True, null=True)
    sum_sqmile = models.FloatField(blank=True, null=True)
    wkb_geometry = GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rlis_neighborhoods'
