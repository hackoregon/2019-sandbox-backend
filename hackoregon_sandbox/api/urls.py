from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views
from api.views import AllSweepsV02ViewSet, RlisNeighborhoodsViewSet, EsciFinalViewSet, LustNotOilClipViewSet, SuperfundViewSet, PortlandMsaNcdbViewSet
                       

router = DefaultRouter()
router.register(r'Tags', views.TagViewSet)
router.register(r'Layers', views.LayerViewSet)
router.register(r'Packages', views.PackageViewSet)
router.register(r'AllSweepsV02s', AllSweepsV02ViewSet)
router.register(r'RlisNeighborhoods', RlisNeighborhoodsViewSet)
router.register(r'LustNotOils', LustNotOilClipViewSet)
router.register(r'PortlandMsaNcdb', PortlandMsaNcdbViewSet)
router.register(r'EsciFinals', EsciFinalViewSet)
router.register(r'Superfunds', SuperfundViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
