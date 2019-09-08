from datetime import datetime
import logging

from api import google_sheets
from api import models


logger = logging.getLogger(__name__)


"""
Indicates status of completion for response rows representing Packages or Layers
"""
class CompletionStatus:    
    UNDEFINED = 'UN'
    COMPLETE = 'CP'
    IN_PROGRESS = 'IP'
    DEFAULT = UNDEFINED

    Choices = (
        (UNDEFINED, 'UN'),
        (COMPLETE, 'Complete'),
        (IN_PROGRESS, 'In Progress'),        
    )

    @classmethod
    def from_string(cls, string):
        for k,v in cls.Choices:
            if v == string:
                return k
        return CompletionStatus.DEFAULT


"""
Create a Layer object from a response row
"""
def create_layer_from_response(row_index):

    row_dictionary = google_sheets.get_layer_row_dictionary(row_index)
    if row_dictionary is not None and len(row_dictionary) > 0:
        
        layer_status = CompletionStatus.from_string(row_dictionary['Layer Status'])
        if layer_status == CompletionStatus.COMPLETE:

            created = datetime.now()
            name = row_dictionary['Layer Name']
            data_endpoint = row_dictionary['Data API Endpoint ']
            metadata_endpoint = row_dictionary['Metadata API Endpoint ']
            creator = row_dictionary['Creator']        
            rating = models.Ratings.from_string(row_dictionary['Rating'])                        
            aggregation_flag = models.AggregationFlags.from_string(row_dictionary['Aggregation Flag'])              

            new_layer = models.Layer(created = created, 
                                    name = name,
                                    data_endpoint = data_endpoint, 
                                    metadata_endpoint = metadata_endpoint,
                                    creator = creator,
                                    #visualization_type = visualization_type,
                                    rating = rating,
                                    aggregation = aggregation_flag)            
            
            new_layer.save()

            tags = row_dictionary['Tags']      
            create_tag_objects(tags, new_layer)

              # dates
            date_field_name = row_dictionary['Date Field Name']
            date_granularity = models.DateGranularities.from_string(row_dictionary['Date Granularity'])            
            default_filter = row_dictionary['Default Date']
            date_min = row_dictionary['Minimum Date']
            date_max = row_dictionary['Maximum Date']

            dates = models.Dates(field_name=date_field_name, granularity=date_granularity, default_filter=default_filter, min=date_min, max=date_max)
            dates.save()

            # create visualization object
            map_type = models.MapTypes.from_string(row_dictionary['Map Type'])                         

            # map = models.Map()
            # map.Save()
            # dashboard = models.VisualizationEntity()
            # dashboard.Save()
            # tooltip = models.VisualizationEntity()            
            # tooltip.Save()          

            # visualization = models.Visualization(map=map, dashboard=dashboard, tooltip=tooltip, dates=dates)
            # visualization.Save()

            return new_layer

    return None


"""
Create a Package object from a response row
"""
def create_package_from_response(row_index):

    row_dictionary = google_sheets.get_package_row_dictionary(row_index)
    if row_dictionary is not None and len(row_dictionary) > 0:

        package_status = CompletionStatus.from_string(row_dictionary['Package Status'])
        if package_status == CompletionStatus.COMPLETE:
            
            created = datetime.now()
            name = row_dictionary['Package Name']
            #metadata_endpoint = row_dictionary['Metadata API Endpoint ']
            contributor = row_dictionary['Contributor'] 
            curation = models.CurationFlags.from_string(row_dictionary['Curation Flag'])                                      

            new_package = models.Package(created = created,
                                         name = name,
                                         #metadata_endpoint = metadata_endpoint,
                                         contributor = contributor,
                                         curation = curation)

            layers_to_add = []
                        
            for layer_index in list(range(1, 7)):
                layer_name =  row_dictionary['Layer '+ str(layer_index)]
                if layer_name:                                  
                    layers_to_add.append(models.Layer.objects.get(name = layer_name))
                              
            addl_layers = row_dictionary['Addl Layers']
            if addl_layers:
                for layer_name in addl_layers.split(','):
                    layers_to_add.append(models.Layer.objects.get(name = layer_name))

            new_package.save()

            for layer_to_add in layers_to_add:
                new_package.layers.add(layer_to_add)

            tags = row_dictionary['Tags']      
            create_tag_objects(tags, new_package)

            return new_package

    return None


"""
Create Tag objects and add them to the tag_parent_object
"""
def create_tag_objects(tag_string, tag_parent_object):    
    tag_pairs = tag_string.split(',')              
    for tag_pair in tag_pairs:
        tag_pair = tag_pair.strip()
        tag_pair_tokens = tag_pair.split('=')
        if len(tag_pair_tokens) == 1:     
            tag_object = models.Tag(name = tag_pair_tokens[0].strip(), value = '')
        elif len(tag_pair_tokens) == 2:
            tag_object = models.Tag(name = tag_pair_tokens[0].strip(), value = tag_pair_tokens[1].strip())        
        tag_object.save()
        tag_parent_object.tags.add(tag_object)
