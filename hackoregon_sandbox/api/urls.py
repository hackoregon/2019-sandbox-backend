from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register(r'Tags', views.TagViewSet)
router.register(r'Layers', views.LayerViewSet)
router.register(r'Packages', views.PackageViewSet)
router.register(r'AllSweepsV02', views.AllSweepsV02ViewSet)
router.register(r'RlisNeighborhoods', views.RlisNeighborhoodsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
