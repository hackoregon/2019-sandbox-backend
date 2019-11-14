# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.gis.db import models


class CommunityGardensV20190122(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    propertyid = models.IntegerField(blank=True, null=True)
    sitename = models.CharField(max_length=50, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    acres = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    r_value = models.IntegerField(blank=True, null=True)
    plotspergarden = models.IntegerField(blank=True, null=True)
    waitlist = models.IntegerField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community_gardens_v2019_01_22'


class ParksV20190129(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    objectid = models.IntegerField(blank=True, null=True)
    propertyid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    acres = models.FloatField(blank=True, null=True)
    shape_length = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parks_v2019_01_29'


class PdxMsa2010CensusBlockGroups(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    tract = models.CharField(max_length=50, blank=True, null=True)
    tract_no = models.FloatField(blank=True, null=True)
    bg = models.CharField(max_length=50, blank=True, null=True)
    trbg = models.CharField(max_length=50, blank=True, null=True)
    fips = models.CharField(max_length=50, blank=True, null=True)
    pop10 = models.IntegerField(blank=True, null=True)
    du10 = models.IntegerField(blank=True, null=True)
    vac10 = models.IntegerField(blank=True, null=True)
    white = models.IntegerField(blank=True, null=True)
    black = models.IntegerField(blank=True, null=True)
    aian = models.IntegerField(blank=True, null=True)
    asian = models.IntegerField(blank=True, null=True)
    nhpi = models.IntegerField(blank=True, null=True)
    other_race = models.IntegerField(blank=True, null=True)
    pop_2_race = models.IntegerField(blank=True, null=True)
    hispanic = models.IntegerField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdx_msa_2010_census_block_groups'


class PdxMsa2010CensusTracts(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=50, blank=True, null=True)
    tract = models.CharField(max_length=50, blank=True, null=True)
    tract_no = models.FloatField(blank=True, null=True)
    fips = models.CharField(max_length=50, blank=True, null=True)
    pop10 = models.IntegerField(blank=True, null=True)
    du10 = models.IntegerField(blank=True, null=True)
    vac10 = models.IntegerField(blank=True, null=True)
    white = models.IntegerField(blank=True, null=True)
    black = models.IntegerField(blank=True, null=True)
    aian = models.IntegerField(blank=True, null=True)
    asian = models.IntegerField(blank=True, null=True)
    nhpi = models.IntegerField(blank=True, null=True)
    other_race = models.IntegerField(blank=True, null=True)
    pop_2_race = models.IntegerField(blank=True, null=True)
    hispanic = models.IntegerField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdx_msa_2010_census_tracts'


class PdxMsaNcdb(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    geo_fips = models.BigIntegerField(blank=True, null=True)
    geo_state = models.IntegerField(blank=True, null=True)
    geo_county = models.IntegerField(blank=True, null=True)
    geo_tract = models.IntegerField(blank=True, null=True)
    cbsa = models.IntegerField(blank=True, null=True)
    metroname = models.CharField(max_length=50, blank=True, null=True)
    tractcontrol = models.IntegerField(blank=True, null=True)
    tractpopulation2010 = models.IntegerField(blank=True, null=True)
    medinc_90 = models.FloatField(blank=True, null=True)
    medinc_00 = models.FloatField(blank=True, null=True)
    medinc_10 = models.FloatField(blank=True, null=True)
    medinc_17 = models.FloatField(blank=True, null=True)
    medhomeval_90 = models.FloatField(blank=True, null=True)
    medhomeval_00 = models.FloatField(blank=True, null=True)
    medhomeval_10 = models.FloatField(blank=True, null=True)
    medhomeval_17 = models.FloatField(blank=True, null=True)
    medrentval_90 = models.FloatField(blank=True, null=True)
    medrentval_00 = models.FloatField(blank=True, null=True)
    medrentval_10 = models.FloatField(blank=True, null=True)
    medrentval_17 = models.FloatField(blank=True, null=True)
    ownshare_90 = models.FloatField(blank=True, null=True)
    ownshare_00 = models.FloatField(blank=True, null=True)
    ownshare_10 = models.FloatField(blank=True, null=True)
    ownshare_17 = models.FloatField(blank=True, null=True)
    whiteshare_90 = models.FloatField(blank=True, null=True)
    whiteshare_00 = models.FloatField(blank=True, null=True)
    whiteshare_10 = models.FloatField(blank=True, null=True)
    whiteshare_17 = models.FloatField(blank=True, null=True)
    blackshare_90 = models.FloatField(blank=True, null=True)
    blackshare_00 = models.FloatField(blank=True, null=True)
    blackshare_10 = models.FloatField(blank=True, null=True)
    blackshare_17 = models.FloatField(blank=True, null=True)
    hispshare_90 = models.FloatField(blank=True, null=True)
    hispshare_00 = models.FloatField(blank=True, null=True)
    hispshare_10 = models.FloatField(blank=True, null=True)
    hispshare_17 = models.FloatField(blank=True, null=True)
    asothshare_90 = models.FloatField(blank=True, null=True)
    asothshare_00 = models.FloatField(blank=True, null=True)
    asothshare_10 = models.FloatField(blank=True, null=True)
    asothshare_17 = models.FloatField(blank=True, null=True)
    rentcbshare_90 = models.FloatField(blank=True, null=True)
    rentcbshare_00 = models.FloatField(blank=True, null=True)
    rentcbshare_10 = models.FloatField(blank=True, null=True)
    rentcbshare_17 = models.FloatField(blank=True, null=True)
    povrate_90 = models.FloatField(blank=True, null=True)
    povrate_00 = models.FloatField(blank=True, null=True)
    povrate_10 = models.FloatField(blank=True, null=True)
    povrate_17 = models.FloatField(blank=True, null=True)
    bachshare_90 = models.FloatField(blank=True, null=True)
    bachshare_00 = models.FloatField(blank=True, null=True)
    bachshare_10 = models.FloatField(blank=True, null=True)
    bachshare_17 = models.FloatField(blank=True, null=True)
    chrent_9017 = models.FloatField(blank=True, null=True)
    chrent_0017 = models.FloatField(blank=True, null=True)
    chrent_1017 = models.FloatField(blank=True, null=True)
    chinc_9017 = models.FloatField(blank=True, null=True)
    chinc_0017 = models.FloatField(blank=True, null=True)
    chinc_1017 = models.FloatField(blank=True, null=True)
    chhomeval_9017 = models.FloatField(blank=True, null=True)
    chhomeval_0017 = models.FloatField(blank=True, null=True)
    chhomeval_1017 = models.FloatField(blank=True, null=True)
    chbachshare_9017 = models.FloatField(blank=True, null=True)
    chbachshare_0017 = models.FloatField(blank=True, null=True)
    chbachshare_1017 = models.FloatField(blank=True, null=True)
    chwhiteshare_9017 = models.FloatField(blank=True, null=True)
    chwhiteshare_0017 = models.FloatField(blank=True, null=True)
    chwhiteshare_1017 = models.FloatField(blank=True, null=True)
    chblackshare_9017 = models.FloatField(blank=True, null=True)
    chblackshare_0017 = models.FloatField(blank=True, null=True)
    chblackshare_1017 = models.FloatField(blank=True, null=True)
    chhispshare_9017 = models.FloatField(blank=True, null=True)
    chhispshare_0017 = models.FloatField(blank=True, null=True)
    chhispshare_1017 = models.FloatField(blank=True, null=True)
    chasothshare_9017 = models.FloatField(blank=True, null=True)
    chasothshare_0017 = models.FloatField(blank=True, null=True)
    chasothshare_1017 = models.FloatField(blank=True, null=True)
    chownshare_9017 = models.FloatField(blank=True, null=True)
    chownshare_0017 = models.FloatField(blank=True, null=True)
    chownshare_1017 = models.FloatField(blank=True, null=True)
    chpovrate_9017 = models.FloatField(blank=True, null=True)
    chpovrate_0017 = models.FloatField(blank=True, null=True)
    chpovrate_1017 = models.FloatField(blank=True, null=True)
    chrentcbshare_9017 = models.FloatField(blank=True, null=True)
    chrentcbshare_0017 = models.FloatField(blank=True, null=True)
    chrentcbshare_1017 = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pdx_msa_ncdb'


"""
"""
class Dataset045Dc(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    geoid = models.CharField(max_length=50, blank=True, null=True)
    metroname = models.CharField(max_length=50, blank=True, null=True)
    whiteshare_90 = models.FloatField(blank=True, null=True)
    whiteshare_00 = models.FloatField(blank=True, null=True)
    whiteshare_10 = models.FloatField(blank=True, null=True)
    whiteshare_17 = models.FloatField(blank=True, null=True)
    blackshare_90 = models.FloatField(blank=True, null=True)
    blackshare_00 = models.FloatField(blank=True, null=True)
    blackshare_10 = models.FloatField(blank=True, null=True)
    blackshare_17 = models.FloatField(blank=True, null=True)
    hispshare_90 = models.FloatField(blank=True, null=True)
    hispshare_00 = models.FloatField(blank=True, null=True)
    hispshare_10 = models.FloatField(blank=True, null=True)
    hispshare_17 = models.FloatField(blank=True, null=True)
    asothshare_90 = models.FloatField(blank=True, null=True)
    asothshare_00 = models.FloatField(blank=True, null=True)
    asothshare_10 = models.FloatField(blank=True, null=True)
    asothshare_17 = models.FloatField(blank=True, null=True)
    chinc_9017 = models.FloatField(blank=True, null=True)
    chinc_0017 = models.FloatField(blank=True, null=True)
    chinc_1017 = models.FloatField(blank=True, null=True)
    medinc_90 = models.FloatField(blank=True, null=True)
    medinc_00 = models.FloatField(blank=True, null=True)
    medinc_10 = models.FloatField(blank=True, null=True)
    medinc_17 = models.FloatField(blank=True, null=True)
    metmedinc_90 = models.FloatField(blank=True, null=True)
    metmedinc_00 = models.FloatField(blank=True, null=True)
    metmedinc_10 = models.FloatField(blank=True, null=True)
    metmedinc_17 = models.FloatField(blank=True, null=True)
    metchinc_9017 = models.FloatField(blank=True, null=True)
    metchinc_9000 = models.FloatField(blank=True, null=True)
    metchinc_0010 = models.FloatField(blank=True, null=True)
    metchinc_0017 = models.FloatField(blank=True, null=True)
    metchinc_1017 = models.FloatField(blank=True, null=True)
    povrate_90 = models.FloatField(blank=True, null=True)
    povrate_00 = models.FloatField(blank=True, null=True)
    povrate_10 = models.FloatField(blank=True, null=True)
    povrate_17 = models.FloatField(blank=True, null=True)
    rentcbshare_90 = models.FloatField(blank=True, null=True)
    rentcbshare_00 = models.FloatField(blank=True, null=True)
    rentcbshare_10 = models.FloatField(blank=True, null=True)
    rentcbshare_17 = models.FloatField(blank=True, null=True)
    metrentcbshare_90 = models.FloatField(blank=True, null=True)
    metrentcbshare_00 = models.FloatField(blank=True, null=True)
    metrentcbshare_10 = models.FloatField(blank=True, null=True)
    metrentcbshare_17 = models.FloatField(blank=True, null=True)
    metchrentcbshare_9017 = models.FloatField(blank=True, null=True)
    metchrentcbshare_9000 = models.FloatField(blank=True, null=True)
    metchrentcbshare_0010 = models.FloatField(blank=True, null=True)
    metchrentcbshare_0017 = models.FloatField(blank=True, null=True)
    metchrentcbshare_1017 = models.FloatField(blank=True, null=True)
    chrent_9017 = models.FloatField(blank=True, null=True)
    chrent_0017 = models.FloatField(blank=True, null=True)
    chrent_1017 = models.FloatField(blank=True, null=True)
    metchrent_9017 = models.FloatField(db_column='metchrent__9017', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    metchrent_9000 = models.FloatField(db_column='metchrent__9000', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    metchrent_0010 = models.FloatField(db_column='metchrent__0010', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    metchrent_0017 = models.FloatField(db_column='metchrent__0017', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    metchrent_1017 = models.FloatField(db_column='metchrent__1017', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    chbachshare_9017 = models.FloatField(blank=True, null=True)
    chbachshare_0017 = models.FloatField(blank=True, null=True)
    chbachshare_1017 = models.FloatField(blank=True, null=True)
    metchbachshare_9017 = models.FloatField(blank=True, null=True)
    metchbachshare_9000 = models.FloatField(blank=True, null=True)
    metchbachshare_0010 = models.FloatField(blank=True, null=True)
    metchbachshare_0017 = models.FloatField(blank=True, null=True)
    metchbachshare_1017 = models.FloatField(blank=True, null=True)
    medhomeval_90 = models.FloatField(blank=True, null=True)
    medhomeval_00 = models.FloatField(blank=True, null=True)
    medhomeval_10 = models.FloatField(blank=True, null=True)
    medhomeval_17 = models.FloatField(blank=True, null=True)
    medrentval_90 = models.FloatField(blank=True, null=True)
    medrentval_00 = models.FloatField(blank=True, null=True)
    medrentval_10 = models.FloatField(blank=True, null=True)
    medrentval_17 = models.FloatField(blank=True, null=True)
    ownshare_90 = models.FloatField(blank=True, null=True)
    ownshare_00 = models.FloatField(blank=True, null=True)
    ownshare_10 = models.FloatField(blank=True, null=True)
    ownshare_17 = models.FloatField(blank=True, null=True)
    bachshare_90 = models.FloatField(blank=True, null=True)
    bachshare_00 = models.FloatField(blank=True, null=True)
    bachshare_10 = models.FloatField(blank=True, null=True)
    bachshare_17 = models.FloatField(blank=True, null=True)
    totalpopulation_90 = models.FloatField(blank=True, null=True)
    totalpopulation_00 = models.FloatField(blank=True, null=True)
    totalpopulation_10 = models.FloatField(blank=True, null=True)
    totalpopulation_17 = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataset045_dc'


"""
"""
class Dataset045Pdx(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    geoid = models.CharField(max_length=50, blank=True, null=True)
    metroname = models.CharField(max_length=50, blank=True, null=True)
    whiteshare_90 = models.FloatField(blank=True, null=True)
    whiteshare_00 = models.FloatField(blank=True, null=True)
    whiteshare_10 = models.FloatField(blank=True, null=True)
    whiteshare_17 = models.FloatField(blank=True, null=True)
    blackshare_90 = models.FloatField(blank=True, null=True)
    blackshare_00 = models.FloatField(blank=True, null=True)
    blackshare_10 = models.FloatField(blank=True, null=True)
    blackshare_17 = models.FloatField(blank=True, null=True)
    hispshare_90 = models.FloatField(blank=True, null=True)
    hispshare_00 = models.FloatField(blank=True, null=True)
    hispshare_10 = models.FloatField(blank=True, null=True)
    hispshare_17 = models.FloatField(blank=True, null=True)
    asothshare_90 = models.FloatField(blank=True, null=True)
    asothshare_00 = models.FloatField(blank=True, null=True)
    asothshare_10 = models.FloatField(blank=True, null=True)
    asothshare_17 = models.FloatField(blank=True, null=True)
    chinc_9017 = models.FloatField(blank=True, null=True)
    chinc_0017 = models.FloatField(blank=True, null=True)
    chinc_1017 = models.FloatField(blank=True, null=True)
    medinc_90 = models.FloatField(blank=True, null=True)
    medinc_00 = models.FloatField(blank=True, null=True)
    medinc_10 = models.FloatField(blank=True, null=True)
    medinc_17 = models.FloatField(blank=True, null=True)
    metmedinc_90 = models.FloatField(blank=True, null=True)
    metmedinc_00 = models.FloatField(blank=True, null=True)
    metmedinc_10 = models.FloatField(blank=True, null=True)
    metmedinc_17 = models.FloatField(blank=True, null=True)
    metchinc_9017 = models.FloatField(blank=True, null=True)
    metchinc_9000 = models.FloatField(blank=True, null=True)
    metchinc_0010 = models.FloatField(blank=True, null=True)
    metchinc_0017 = models.FloatField(blank=True, null=True)
    metchinc_1017 = models.FloatField(blank=True, null=True)
    povrate_90 = models.FloatField(blank=True, null=True)
    povrate_00 = models.FloatField(blank=True, null=True)
    povrate_10 = models.FloatField(blank=True, null=True)
    povrate_17 = models.FloatField(blank=True, null=True)
    rentcbshare_90 = models.FloatField(blank=True, null=True)
    rentcbshare_00 = models.FloatField(blank=True, null=True)
    rentcbshare_10 = models.FloatField(blank=True, null=True)
    rentcbshare_17 = models.FloatField(blank=True, null=True)
    metrentcbshare_90 = models.FloatField(blank=True, null=True)
    metrentcbshare_00 = models.FloatField(blank=True, null=True)
    metrentcbshare_10 = models.FloatField(blank=True, null=True)
    metrentcbshare_17 = models.FloatField(blank=True, null=True)
    metchrentcbshare_9017 = models.FloatField(blank=True, null=True)
    metchrentcbshare_9000 = models.FloatField(blank=True, null=True)
    metchrentcbshare_0010 = models.FloatField(blank=True, null=True)
    metchrentcbshare_0017 = models.FloatField(blank=True, null=True)
    metchrentcbshare_1017 = models.FloatField(blank=True, null=True)
    chrent_9017 = models.FloatField(blank=True, null=True)
    chrent_0017 = models.FloatField(blank=True, null=True)
    chrent_1017 = models.FloatField(blank=True, null=True)
    metchrent_9017 = models.FloatField(db_column='metchrent__9017', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    metchrent_9000 = models.FloatField(db_column='metchrent__9000', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    metchrent_0010 = models.FloatField(db_column='metchrent__0010', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    metchrent_0017 = models.FloatField(db_column='metchrent__0017', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    metchrent_1017 = models.FloatField(db_column='metchrent__1017', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    chbachshare_9017 = models.FloatField(blank=True, null=True)
    chbachshare_0017 = models.FloatField(blank=True, null=True)
    chbachshare_1017 = models.FloatField(blank=True, null=True)
    metchbachshare_9017 = models.FloatField(blank=True, null=True)
    metchbachshare_9000 = models.FloatField(blank=True, null=True)
    metchbachshare_0010 = models.FloatField(blank=True, null=True)
    metchbachshare_0017 = models.FloatField(blank=True, null=True)
    metchbachshare_1017 = models.FloatField(blank=True, null=True)
    medhomeval_90 = models.FloatField(blank=True, null=True)
    medhomeval_00 = models.FloatField(blank=True, null=True)
    medhomeval_10 = models.FloatField(blank=True, null=True)
    medhomeval_17 = models.FloatField(blank=True, null=True)
    medrentval_90 = models.FloatField(blank=True, null=True)
    medrentval_00 = models.FloatField(blank=True, null=True)
    medrentval_10 = models.FloatField(blank=True, null=True)
    medrentval_17 = models.FloatField(blank=True, null=True)
    ownshare_90 = models.FloatField(blank=True, null=True)
    ownshare_00 = models.FloatField(blank=True, null=True)
    ownshare_10 = models.FloatField(blank=True, null=True)
    ownshare_17 = models.FloatField(blank=True, null=True)
    bachshare_90 = models.FloatField(blank=True, null=True)
    bachshare_00 = models.FloatField(blank=True, null=True)
    bachshare_10 = models.FloatField(blank=True, null=True)
    bachshare_17 = models.FloatField(blank=True, null=True)
    totalpopulation_90 = models.FloatField(blank=True, null=True)
    totalpopulation_00 = models.FloatField(blank=True, null=True)
    totalpopulation_10 = models.FloatField(blank=True, null=True)
    totalpopulation_17 = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataset045_pdx'

class NvB28002(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    geoid = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    b28002_001e = models.FloatField(blank=True, null=True)
    b28002_001m = models.FloatField(blank=True, null=True)
    b28002_002e = models.FloatField(blank=True, null=True)
    b28002_002m = models.FloatField(blank=True, null=True)
    b28002_003e = models.FloatField(blank=True, null=True)
    b28002_003m = models.FloatField(blank=True, null=True)
    b28002_004e = models.FloatField(blank=True, null=True)
    b28002_004m = models.FloatField(blank=True, null=True)
    b28002_005e = models.FloatField(blank=True, null=True)
    b28002_005m = models.FloatField(blank=True, null=True)
    b28002_006e = models.FloatField(blank=True, null=True)
    b28002_006m = models.FloatField(blank=True, null=True)
    b28002_007e = models.FloatField(blank=True, null=True)
    b28002_007m = models.FloatField(blank=True, null=True)
    b28002_008e = models.FloatField(blank=True, null=True)
    b28002_008m = models.FloatField(blank=True, null=True)
    b28002_009e = models.FloatField(blank=True, null=True)
    b28002_009m = models.FloatField(blank=True, null=True)
    b28002_010e = models.FloatField(blank=True, null=True)
    b28002_010m = models.FloatField(blank=True, null=True)
    b28002_011e = models.FloatField(blank=True, null=True)
    b28002_011m = models.FloatField(blank=True, null=True)
    b28002_012e = models.FloatField(blank=True, null=True)
    b28002_012m = models.FloatField(blank=True, null=True)
    b28002_013e = models.FloatField(blank=True, null=True)
    b28002_013m = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nv_b28002'

class NvB28010(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    geoid = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    b28010_001e = models.FloatField(blank=True, null=True)
    b28010_001m = models.FloatField(blank=True, null=True)
    b28010_002e = models.FloatField(blank=True, null=True)
    b28010_002m = models.FloatField(blank=True, null=True)
    b28010_003e = models.FloatField(blank=True, null=True)
    b28010_003m = models.FloatField(blank=True, null=True)
    b28010_004e = models.FloatField(blank=True, null=True)
    b28010_004m = models.FloatField(blank=True, null=True)
    b28010_005e = models.FloatField(blank=True, null=True)
    b28010_005m = models.FloatField(blank=True, null=True)
    b28010_006e = models.FloatField(blank=True, null=True)
    b28010_006m = models.FloatField(blank=True, null=True)
    b28010_007e = models.FloatField(blank=True, null=True)
    b28010_007m = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nv_b28010'

class GaB28002(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    geoid = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    b28002_001e = models.FloatField(blank=True, null=True)
    b28002_001m = models.FloatField(blank=True, null=True)
    b28002_002e = models.FloatField(blank=True, null=True)
    b28002_002m = models.FloatField(blank=True, null=True)
    b28002_003e = models.FloatField(blank=True, null=True)
    b28002_003m = models.FloatField(blank=True, null=True)
    b28002_004e = models.FloatField(blank=True, null=True)
    b28002_004m = models.FloatField(blank=True, null=True)
    b28002_005e = models.FloatField(blank=True, null=True)
    b28002_005m = models.FloatField(blank=True, null=True)
    b28002_006e = models.FloatField(blank=True, null=True)
    b28002_006m = models.FloatField(blank=True, null=True)
    b28002_007e = models.FloatField(blank=True, null=True)
    b28002_007m = models.FloatField(blank=True, null=True)
    b28002_008e = models.FloatField(blank=True, null=True)
    b28002_008m = models.FloatField(blank=True, null=True)
    b28002_009e = models.FloatField(blank=True, null=True)
    b28002_009m = models.FloatField(blank=True, null=True)
    b28002_010e = models.FloatField(blank=True, null=True)
    b28002_010m = models.FloatField(blank=True, null=True)
    b28002_011e = models.FloatField(blank=True, null=True)
    b28002_011m = models.FloatField(blank=True, null=True)
    b28002_012e = models.FloatField(blank=True, null=True)
    b28002_012m = models.FloatField(blank=True, null=True)
    b28002_013e = models.FloatField(blank=True, null=True)
    b28002_013m = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ga_b28002'


class GaB28010(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    geoid = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    b28010_001e = models.FloatField(blank=True, null=True)
    b28010_001m = models.FloatField(blank=True, null=True)
    b28010_002e = models.FloatField(blank=True, null=True)
    b28010_002m = models.FloatField(blank=True, null=True)
    b28010_003e = models.FloatField(blank=True, null=True)
    b28010_003m = models.FloatField(blank=True, null=True)
    b28010_004e = models.FloatField(blank=True, null=True)
    b28010_004m = models.FloatField(blank=True, null=True)
    b28010_005e = models.FloatField(blank=True, null=True)
    b28010_005m = models.FloatField(blank=True, null=True)
    b28010_006e = models.FloatField(blank=True, null=True)
    b28010_006m = models.FloatField(blank=True, null=True)
    b28010_007e = models.FloatField(blank=True, null=True)
    b28010_007m = models.FloatField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ga_b28010'
        
class CensusVariables(models.Model):
    name = models.TextField(primary_key=True)
    label = models.TextField(blank=True, null=True)
    concept = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'census_variables'

class TractNames(models.Model):
    geoid = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tract_names'

class InternetStats(models.Model):
    geoid = models.ForeignKey(TractNames, models.DO_NOTHING, db_column='geoid', blank=True, null=True)
    variable = models.ForeignKey(CensusVariables, models.DO_NOTHING, db_column='variable', blank=True, null=True)
    estimate = models.FloatField(blank=True, null=True)
    moe_90pct = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internet_stats'
