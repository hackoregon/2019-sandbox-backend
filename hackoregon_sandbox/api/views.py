from rest_framework import viewsets, permissions
from django.http import HttpResponse
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import render

from api import (models, 
                 preexisting_models, 
                 model_parsing, 
                 packages)

from api.serializers import (LayerSerializer, 
                             TagSerializer, 
                             PackageSerializer, 
                             DatesSerializer, 
                             VisualizationSerializer,
                             IconMappingSerializer,
                             ColorAreaSerializer,
                             MapSerializer, 
                             VisualizationEntitySerializer,
                             VisualizationEntityObjectSerializer)

from api.serializers import (PdxMsa2010CensusBlockGroupsSerializer, 
                             PdxMsa2010CensusTractsSerializer, 
                             PdxMsaNcdbSerializer,
                             ParksV20190129Serializer, 
                             CommunityGardensV20190122Serializer,
                             Dataset045PdxSerializer, 
                             Dataset045DcSerializer)

from api.serializers import NvB28002Serializer, NvB28010Serializer, GaB28002Serializer, GaB28010Serializer
from api.serializers import CensusVariablesSerializer, TractNamesSerializer, InternetStatsSerializer

PACKAGES_JSON_FILE = "/code/src_files/packages.json"


def index(request):
    context = {}
    return render(request, 'api/index.html', context)


"""
"""
def create_layer(request): 
    row_param = request.GET.get('row')    
    if row_param is not None:     
        try:   
            row_index = int(row_param)  
            model_parsing.create_layer_from_response(row_index)   
            return HttpResponse('<h1>Success!:<br/></h1>'
                                '<h2>Package was created successfully (from row: {})</h2>'.format(row_param))
        except IndexError:
            return HttpResponse('<h1>Failure!:<br/></h1>'
                                '<h2>Layer creation failed (from row: {})<br/></h2>'.format(row_param) + 
                                '<h3>Index was out of range</h3>')
        except IntegrityError:
            return HttpResponse('<h1>Failure!:<br/></h1>'
                                '<h2>Layer creation failed (from row: {})<br/></h2>'.format(row_param) + 
                                '<h3>Layer already exists</h3>')
    else:
        return HttpResponse('<h1>Failed!:<br/></h1>'
                            '<h2>Row param did not exist</h2>')

"""
"""
def create_package(request): 
    row_param = request.GET.get('row')    
    if row_param is not None:        
        try:   
            row_index = int(row_param)  
            model_parsing.create_package_from_response(row_index)   
            return HttpResponse('<h1>Success!ModelViewSet:<br/></h1>'
                                '<h2>Package ModelViewSetwas created successfully (from row: {})</h2>'.format(row_param))
        except IndexError:
            return HttpResponse('<h1>Failure!ModelViewSet:<br/></h1>'
                                '<h2>Package creation failed (from row: {})<br/></h2>'.format(row_param) + 
                                '<h3>Index was out of range</h3>')
        except IntegrityError:
            return HttpResponse('<h1>Failure!:<br/></h1>'
                                '<h2>Package creation failed (from row: {})<br/></h2>'.format(row_param) + 
                                '<h3>Package already exists</h3>')
    else:
        return HttpResponse('<h1>Failed!:<br/></h1>'
                            '<h2>Row param did not exist</h2>')


"""
"""
def package_info_view(request):
    return JsonResponse(packages.load_json_from_file(PACKAGES_JSON_FILE), safe=False)

"""
"""
class LayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Layer to be viewed or listed.
    """
    queryset = models.Layer.objects.all()
    serializer_class = LayerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

"""
"""
class IconMappingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Layer to be viewed or listed.
    """
    queryset = models.IconMapping.objects.all()
    serializer_class = IconMappingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

"""
"""
class ColorAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Layer to be viewed or listed.
    """
    queryset = models.ColorArea.objects.all()
    serializer_class = ColorAreaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

"""
"""
class MapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Layer to be viewed or listed.
    """
    queryset = models.Map.objects.all()
    serializer_class = MapSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

"""
"""
class VisualizationEntityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Layer to be viewed or listed.
    """
    queryset = models.VisualizationEntity.objects.all()
    serializer_class = VisualizationEntitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

"""
"""
class VisualizationEntityObjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Layer to be viewed or listed.
    """
    queryset = models.VisualizationEntityObject.objects.all()
    serializer_class = VisualizationEntityObjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
       
"""
Tags
"""
class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tag to be viewed or listed.
    """
    queryset = models.Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

"""
"""
class PackageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = models.Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


"""

"""
class DatesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = models.Dates.objects.all()
    serializer_class = DatesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

"""
Visualizations
"""
class VisualizationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tag to be viewed or listed.
    """
    queryset = models.Visualization.objects.all()
    serializer_class = VisualizationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

"""
"""
class PdxMsa2010CensusBlockGroupsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = preexisting_models.PdxMsa2010CensusBlockGroups.objects.all()
    serializer_class = PdxMsa2010CensusBlockGroupsSerializer

"""
"""
class PdxMsa2010CensusTractsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = preexisting_models.PdxMsa2010CensusTracts.objects.all()
    serializer_class = PdxMsa2010CensusTractsSerializer

"""
"""
class PdxMsaNcdbViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = preexisting_models.PdxMsaNcdb.objects.all()
    serializer_class = PdxMsaNcdbSerializer

"""
"""
class ParksV20190129ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows ParksV20190129 to be viewed or listed.
    """
    queryset = preexisting_models.ParksV20190129.objects.all()
    serializer_class = ParksV20190129Serializer

"""
"""
class CommunityGardensV20190122ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV201901esttag to be viewed or listed.
    """
    queryset = preexisting_models.CommunityGardensV20190122.objects.all()
    serializer_class = CommunityGardensV20190122Serializer

"""
"""
class Dataset045PdxViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
    """
    queryset = preexisting_models.Dataset045Pdx.objects.all()
    serializer_class = Dataset045PdxSerializer

"""
"""
class Dataset045DcViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
    """
    queryset = preexisting_models.Dataset045Dc.objects.all()
    serializer_class = Dataset045DcSerializer

"""
"""
class NvB28002ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
    """
    queryset = preexisting_models.NvB28002.objects.all()
    serializer_class = NvB28002Serializer

class NvB28010ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
    """
    queryset = preexisting_models.NvB28010.objects.all()
    serializer_class = NvB28010Serializer

class GaB28002ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
    """
    queryset = preexisting_models.GaB28002.objects.all()
    serializer_class = GaB28002Serializer

class GaB28010ViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
    """
    queryset = preexisting_models.GaB28010.objects.all()
    serializer_class = GaB28010Serializer

class CensusVariablesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
    """
    queryset = preexisting_models.CensusVariables.objects.all()
    serializer_class = CensusVariablesSerializer

class TractNamesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
    """
    queryset = preexisting_models.TractNames.objects.all()
    serializer_class = TractNamesSerializer

class InternetStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
    """
    queryset = preexisting_models.InternetStats.objects.all()
    serializer_class = InternetStatsSerializer