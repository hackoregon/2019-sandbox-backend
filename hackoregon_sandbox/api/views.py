from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from api.models import Tag, Layer, Package
from api.preexisting_models import RlisNeighborhoods, AllSweepsV02
from api.preexisting_models2 import EsciFinal, LustNotOilClip, Superfund, PortlandMsaNcdb
from api.serializers import TagSerializer, LayerSerializer, PackageSerializer, AllSweepsV02Serializer, RlisNeighborhoodsSerializer, EsciFinalSerializer, LustNotOilClipSerializer, SuperfundSerializer, PortlandMsaNcdbSerializer


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

class EsciFinalViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = EsciFinal.objects.all()
    serializer_class = EsciFinalSerializer

class SuperfundViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = Superfund.objects.all()
    serializer_class = SuperfundSerializer

class PortlandMsaNcdbViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = PortlandMsaNcdb.objects.all()
    serializer_class = PortlandMsaNcdbSerializer

class LustNotOilClipViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = LustNotOilClip.objects.all()
    serializer_class = LustNotOilClipSerializer