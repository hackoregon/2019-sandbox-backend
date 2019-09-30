from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

api_title = 'Hack Oregon Sandbox 2019 API'

schema_view = get_swagger_view(title=api_title)


urlpatterns = [
    url(r'^sandbox/schema/', schema_view),
    url(r'^sandbox/api/', include('hackoregon_sandbox.api.urls')),
    url(r'^sandbox/docs/', include_docs_urls(title=api_title)),
    url(r'^sandbox/health/', include('health_check.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
