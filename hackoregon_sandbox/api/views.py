from rest_framework import viewsets
from django.http import HttpResponse
from django.db import IntegrityError
from django.http import JsonResponse

from api import models
from api import preexisting_models
from api.serializers import LayerSerializer, TagSerializer, PackageSerializer, DatesSerializer
from api.serializers import PdxMsa2010CensusBlockGroupsSerializer, PdxMsa2010CensusTractsSerializer, PdxMsaNcdbSerializer
from api.serializers import ParksV20190129Serializer, CommunityGardensV20190122Serializer
from api.serializers import Dataset045PdxSerializer, Dataset045DcSerializer
from api import model_parsing
from api import packages


PACKAGES_JSON_FILE = "/code/src_files/packages.json"


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
        except IndexError:ModelViewSet
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
       
"""
Tags
"""
class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tag to be viewed or listed.
    """
    queryset = models.Tag.objects.all()
    serializer_class = TagSerializer

"""
"""
class PackageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = models.Package.objects.all()
    serializer_class = PackageSerializer


"""

"""
class DatesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = models.Dates.objects.all()
    serializer_class = DatesSerializer

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
    API endpoint that allows CommunityGardensV2019012 to be viewed or listed.
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
