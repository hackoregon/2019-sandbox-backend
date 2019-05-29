from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, detail_route
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from api.models import Tag, Layer, Package
from api.serializers import TagSerializer, LayerSerializer, PackageSerializer


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