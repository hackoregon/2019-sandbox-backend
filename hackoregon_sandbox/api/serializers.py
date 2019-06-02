from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from api.models import Tag, Layer, Package
from api.preexisting_models import AllSweepsV02, RlisNeighborhoods
from api.preexisting_models2 import EsciFinal, LustNotOilClip, Superfund, PortlandMsaNcdb


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


class AllSweepsV02Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = AllSweepsV02
        fields = '__all__'
        geo_field = 'wkb_geometry'


class RlisNeighborhoodsSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = RlisNeighborhoods
        fields = '__all__'
        geo_field = 'wkb_geometry'


class EsciFinalSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = EsciFinal
        fields = '__all__'
        geo_field = 'wkb_geometry'


class LustNotOilClipSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = LustNotOilClip
        fields = '__all__'
        geo_field = 'wkb_geometry'


class PortlandMsaNcdbSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PortlandMsaNcdb
        fields = '__all__'
        geo_field = 'wkb_geometry'
        

class SuperfundSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Superfund
        fields = '__all__'
        geo_field = 'wkb_geometry'

