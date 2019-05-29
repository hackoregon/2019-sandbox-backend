from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()

schema_view = get_swagger_view(title='Hack Oregon Sandbox 2019 API')


urlpatterns = [
    url(r'^sandbox/schema/', schema_view),
    url(r'^sandbox/api/', include('hackoregon_sandbox.api.urls')),
]
