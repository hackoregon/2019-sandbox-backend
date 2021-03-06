from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views
                       

router = DefaultRouter()
router.register(r'PdxMsa2010CensusBlockGroups', views.PdxMsa2010CensusBlockGroupsViewSet)
router.register(r'PdxMsa2010CensusTracts', views.PdxMsa2010CensusTractsViewSet)
router.register(r'PdxMsaNcdbs', views.PdxMsaNcdbViewSet)
router.register(r'ParksV20190129', views.ParksV20190129ViewSet)
router.register(r'CommunityGardensV20190122', views.CommunityGardensV20190122ViewSet)
router.register(r'Dataset045Pdxs', views.Dataset045PdxViewSet)
router.register(r'Dataset045Dcs', views.Dataset045DcViewSet)

router.register(r'Tags', views.TagViewSet)
router.register(r'Layers', views.LayerViewSet)
router.register(r'Packages', views.PackageViewSet)
router.register(r'Visualizations', views.VisualizationViewSet)
router.register(r'Dates', views.DatesViewSet)
router.register(r'IconMappings', views.IconMappingViewSet)
router.register(r'ColorAreas', views.ColorAreaViewSet)
router.register(r'Maps', views.MapViewSet)
router.register(r'VisualizationEntityObjects', views.VisualizationEntityObjectViewSet)
router.register(r'VisualizationEntitys', views.VisualizationEntityViewSet)

router.register(r'NvB28002', views.NvB28002ViewSet)
router.register(r'NvB28010', views.NvB28010ViewSet)
router.register(r'GaB28002', views.GaB28002ViewSet)
router.register(r'GaB28010', views.GaB28010ViewSet)
router.register(r'InternetStats', views.InternetStatsViewSet)
router.register(r'CensusVariables', views.CensusVariablesViewSet)
router.register(r'TractNames', views.TractNamesViewSet)

urlpatterns = [
    url(r'^create_layer/', views.create_layer, name='create_layer'),
    url(r'^create_package/', views.create_package, name='create_package'),
    url(r'^package_info/', views.package_info_view, name='package_info_view'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),        
]
