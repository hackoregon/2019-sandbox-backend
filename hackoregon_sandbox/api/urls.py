from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views
from api.views import PdxMsa2010CensusBlockGroupsViewSet, PdxMsa2010CensusTractsViewSet, PdxMsaNcdbViewSet
                       

router = DefaultRouter()
router.register(r'Tags', views.TagViewSet)
router.register(r'Layers', views.LayerViewSet)
router.register(r'Packages', views.PackageViewSet)
router.register(r'PdxMsa2010CensusBlockGroups', views.PdxMsa2010CensusBlockGroupsViewSet)
router.register(r'PdxMsa2010CensusTracts', PdxMsa2010CensusTractsViewSet)
router.register(r'PdxMsaNcdbs', PdxMsaNcdbViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
