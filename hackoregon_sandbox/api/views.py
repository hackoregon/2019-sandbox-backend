from rest_framework import viewsets
from django.http import HttpResponse

from api import models
from api import preexisting_models
from api.serializers import LayerSerializer, TagSerializer, PackageSerializer
from api.serializers import PdxMsa2010CensusBlockGroupsSerializer, PdxMsa2010CensusTractsSerializer, PdxMsaNcdbSerializer
from api import model_parsing


"""

"""
def create_layer(request): 
    row_param = request.GET.get('row')    
    if row_param is not None:        
        row_index = int(row_param)  
        model_parsing.create_layer_from_response(row_index)   
        return HttpResponse("<h1>Success!:<br/> layer was created successfully from row: " + row_param + "</h1>")                              
    else:
        return HttpResponse("<h1>Failed!:<br/> row param did not exist</h1>")      

"""

"""
def create_package(request): 
    row_param = request.GET.get('row')    
    if row_param is not None:        
        row_index = int(row_param)  
        model_parsing.create_package_from_response(row_index)   
        return HttpResponse("<h1>Success!:<br/> package was created from row: " + row_param + "</h1>")                              
    else:
        return HttpResponse("<h1>Failed!:<br/> row param did not exist</h1>")    


"""

"""
class LayerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Layer to be viewed or listed.
    """
    queryset = models.Layer.objects.all()
    serializer_class = LayerSerializer
       
"""
Tags
"""
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Tag to be viewed or listed.
    """
    queryset = models.Tag.objects.all()
    serializer_class = TagSerializer

"""

"""
class PackageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Package to be viewed or listed.
    """
    queryset = models.Package.objects.all()
    serializer_class = PackageSerializer

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
