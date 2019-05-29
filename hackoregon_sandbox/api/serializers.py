from rest_framework import serializers
#from rest_framework_gis import serializers

from api.models import Tag, Layer, Package


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