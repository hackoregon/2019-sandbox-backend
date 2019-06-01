from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from api.models import Tag, Layer, Package
from api.preexisting_models import RlisNeighborhoods, AllSweepsV02
from api.serializers import TagSerializer, LayerSerializer, PackageSerializer, RlisNeighborhoodsSerializer, AllSweepsV02Serializer


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


class AllSweepsV02ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = AllSweepsV02.objects.all()
    serializer_class = AllSweepsV02Serializer


class RlisNeighborhoodsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = RlisNeighborhoods.objects.all()
    serializer_class = RlisNeighborhoodsSerializer