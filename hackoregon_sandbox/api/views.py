from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from api.models import Tag, Layer, Package
from api.preexisting_models import PdxMsa2010CensusBlockGroups, PdxMsa2010CensusTracts, PdxMsaNcdb
from api.serializers import TagSerializer, LayerSerializer, PackageSerializer, PdxMsa2010CensusBlockGroupsSerializer, PdxMsa2010CensusTractsSerializer, PdxMsaNcdbSerializer


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Tag to be viewed or listed.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class LayerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Layer to be viewed or listed.
    """
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer


class PackageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class PdxMsa2010CensusBlockGroupsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = PdxMsa2010CensusBlockGroups.objects.all()
    serializer_class = PdxMsa2010CensusBlockGroupsSerializer


class PdxMsa2010CensusTractsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = PdxMsa2010CensusTracts.objects.all()
    serializer_class = PdxMsa2010CensusTractsSerializer


class PdxMsaNcdbViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = PdxMsaNcdb.objects.all()
    serializer_class = PdxMsaNcdbSerializer
