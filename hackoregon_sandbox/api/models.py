from django.contrib.gis.db import models
from django.utils import timezone


"""
"""
class VisualizationTypes:    
    UNDEFINED = 'UN'
    PATHMAP = 'PM'
    ICONMAP = 'IM'
    SMALLPOLYGONMAP = 'SP'
    SCATTERPLOTMAP = "SM"
    TEXT = "TX"
    CHLOROPLETHMAP = 'CM'
    DEFAULT = UNDEFINED


    Choices = (
        (UNDEFINED, 'UN'),
        (PATHMAP, 'Path Map'),
        (ICONMAP, 'Icon Map'),
        (SMALLPOLYGONMAP, 'Small Polygon Map'),
        (SCATTERPLOTMAP, 'ScatterPlot Map'),
        (TEXT, 'Text'),
        (CHLOROPLETHMAP, 'Choropleth Map'),
    )

    @classmethod
    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return VisualizationTypes.UNDEFINED


"""
"""
class Ratings:
    UNDEFINED = "UN"
    OPEN = "OP"
    CURATED = "CU"
    BLOCKED = "BL"
    DEFAULT = UNDEFINED

    Choices = (
        (UNDEFINED, "UN"),
        (OPEN, 'Open'),
        (CURATED, 'Curated'),
        (BLOCKED, 'Blocked'),
    )

    @classmethod
    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return Ratings.UNDEFINED    

"""
"""
class CurationFlags:
    UNDEFINED = "UN"
    CIVIC_CURATED = "CC"
    CIVIC_ENDORSED = "CE"
    CONTRIBUTOR_ASSEMBLED = "CA"
    USER_ASSEMBLED = "UA"
    DEFAULT = UNDEFINED

    Choices =  (
        (UNDEFINED, "UN"),
        (CIVIC_CURATED, 'Civic Curated'),
        (CIVIC_ENDORSED, 'Civic Endorsed'),
        (CONTRIBUTOR_ASSEMBLED, 'Contributor Assembled'),
        (USER_ASSEMBLED, 'User Assembled'),
    )

    @classmethod
    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k    
        return CurationFlags.UNDEFINED    


"""
"""
class AggregationFlags:
    UNDEFINED = "UN"
    AGGREGATABLE = "AG"
    AGGREGATE_BY = "AB"
    PRE_AGGREGATED = "PA"
    NONE = "NO"
    DEFAULT = NONE

    Choices = (
        (UNDEFINED, "UN"),
        (AGGREGATABLE, 'Aggregatable'),
        (AGGREGATE_BY, 'Aggregate By'),
        (PRE_AGGREGATED, 'Pre-Aggregated'),
        (NONE, 'None'),
    )

    @classmethod
    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return AggregationFlags.UNDEFINED


"""
"""
class Tag(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)


"""
"""
class Layer(models.Model):
    VERSION = 0
    index = models.CharField(max_length=50)
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(auto_now=True)    
    name = models.CharField(max_length=50)
    version = models.IntegerField()
    data_endpoint = models.URLField()
    metadata_endpoint = models.URLField()
    rating = models.CharField(max_length=2, choices=Ratings.Choices, default=Ratings.DEFAULT)
    visualization_type = models.CharField(max_length=2, choices=VisualizationTypes.Choices, default=VisualizationTypes.DEFAULT)
    creator = models.CharField(max_length=50)
    aggregation = models.CharField(max_length=2, choices=AggregationFlags.Choices, default=AggregationFlags.DEFAULT)    
    tags = models.ManyToManyField(Tag)    


"""
"""
class Package(models.Model):
    index = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    metadata_endpoint = models.URLField()    
    created = models.DateTimeField(null=True)
    modified = models.DateTimeField(auto_now=True)   
    version = models.IntegerField(null=True)
    contributor = models.CharField(max_length=50, null=True)
    curation = models.CharField(max_length=2, choices=CurationFlags.Choices, default=CurationFlags.DEFAULT)
    layers = models.ManyToManyField(Layer)
    #affiliation
