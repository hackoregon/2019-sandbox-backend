from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views
from api.views import AllSweepsV02ViewSet, RlisNeighborhoodsViewSet


router = DefaultRouter()
router.register(r'Tags', views.TagViewSet)
router.register(r'Layers', views.LayerViewSet)
router.register(r'Packages', views.PackageViewSet)
router.register(r'AllSweepsV02', AllSweepsV02ViewSet)
router.register(r'RlisNeighborhoods', RlisNeighborhoodsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
