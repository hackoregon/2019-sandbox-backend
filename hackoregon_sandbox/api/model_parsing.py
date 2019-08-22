from datetime import datetime

from api import google_sheets
from api import models


"""

"""
def create_layer_from_response(row_index):

    row_dictionary = google_sheets.get_layer_row_dictionary(row_index)
    if row_dictionary is not None and len(row_dictionary) > 0:
        
        created = datetime.now()
        name = row_dictionary['Layer Name']
        data_endpoint = row_dictionary['Data API Endpoint ']
        metadata_endpoint = row_dictionary['Metadata API Endpoint ']
        creator = row_dictionary['Creator']
        aggregation_flag = models.AggregationFlags.from_string(row_dictionary['Aggregation Flag'])
        rating = models.Ratings.from_string(row_dictionary['Rating'])
        visualization_type = models.VisualizationTypes.from_string(row_dictionary['Map Type'])               

        new_layer = models.Layer(created = created, 
                                 name = name,
                                 data_endpoint = data_endpoint, 
                                 metadata_endpoint = metadata_endpoint,
                                 creator = creator,
                                 visualization_type = visualization_type,
                                 rating = rating,
                                 aggregation = aggregation_flag)
        
        new_layer.save()

        tags = row_dictionary['Tags']      
        create_tag_objects(tags, new_layer)


def create_package_from_response(row_index):

        row_dictionary = google_sheets.get_package_row_dictionary(row_index)
        if row_dictionary is not None and len(row_dictionary) > 0:
                
                created = datetime.now()
                name = row_dictionary['Package Name']
                #metadata_endpoint = row_dictionary['Metadata API Endpoint ']
                contributor = row_dictionary['Contributor'] 
                curation = models.CurationFlags.from_string(row_dictionary['Curation Flag'])   
                layer1 =  row_dictionary['Layer 1']                          
                layer2 =  row_dictionary['Layer 2']                          
        
                new_package = models.Package(created = created,
                                             name = name,
                                             #metadata_endpoint = metadata_endpoint,
                                             contributor = contributor,
                                             curation = curation)
                
                new_package.save()
        
                tags = row_dictionary['Tags']      
                create_tag_objects(tags, new_package)

"""

"""
def create_tag_objects(tag_string, tag_parent_object):
    tag_names = tag_string.split(',')              
    for tag_name in tag_names:
        tag_object = models.Tag(name = tag_name, value = '')
        tag_object.save()    
        tag_parent_object.tags.add(tag_object)    
