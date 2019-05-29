from django.contrib.gis.db import models


"""
"""
class VisualizationTypes:
    SCATTERPLOTMAP = "SM"
    TEXT = "TX"
    CHLOROPLETHMAP = 'CM'

    Choices = (
        (SCATTERPLOTMAP, 'ScatterPlotMap'),
        (TEXT, 'Text'),
        (CHLOROPLETHMAP, 'ChoroplethMap'),
    )


"""
"""
class Ratings:
    OPEN = "OP"
    CURATED = "CU"
    BLOCKED = "BL"

    Choices = (
        (OPEN, 'Open'),
        (CURATED, 'Curated'),
        (BLOCKED, 'Blocked'),
    )


"""
"""
class CurationFlags:
    CIVIC_CURATED = "CC"
    CIVIC_ENDORSED = "CE"
    CONTRIBUTOR_ASSEMBLED = "CA"
    USER_ASSEMBLED = "UA"

    Choices =  (
        (CIVIC_CURATED, 'Civic Curated'),
        (CIVIC_ENDORSED, 'Civic Endorsed'),
        (CONTRIBUTOR_ASSEMBLED, 'Contributor Assembled'),
        (USER_ASSEMBLED, 'User Assembled'),
    )


"""
"""
class Tag(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)


"""
"""
class Package(models.Model):
    index = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    metadata_endpoint = models.URLField()
    creator = models.CharField(max_length=50)


"""
"""
class Layer(models.Model):
    index = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    version = models.IntegerField()
    data_endpoint = models.URLField()
    metadata_endpoint = models.URLField()
    rating = models.CharField(max_length=2, choices=Ratings.Choices, default=Ratings.OPEN)
    visualization_type = models.CharField(max_length=2, choices=VisualizationTypes.Choices, default=VisualizationTypes.SCATTERPLOTMAP)
    tags = models.ManyToManyField(Tag)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)
    creator = models.CharField(max_length=50)
