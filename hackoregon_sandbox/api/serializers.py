from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from api.models import Tag, Layer, Package
from api.preexisting_models import PdxMsa2010CensusBlockGroups, PdxMsa2010CensusTracts, PdxMsaNcdb


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class LayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Layer
        fields = '__all__'


class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class PdxMsa2010CensusBlockGroupsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PdxMsa2010CensusBlockGroups
        fields = '__all__'
        geo_field = 'wkb_geometry'


class PdxMsa2010CensusTractsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PdxMsa2010CensusTracts
        fields = '__all__'
        geo_field = 'wkb_geometry'


class PdxMsaNcdbSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PdxMsaNcdb
        fields = '__all__'
        geo_field = 'wkb_geometry'
