"""core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include, re_path
from products.urls import products_api
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="DRF Example API",
      default_version='v1',
      description="DRF Example Open API spec",
      terms_of_service=""
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

swagger_api = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    ),
]

api_urls = [
    path('', include(products_api)),
]

urlpatterns = [
    path('', include(swagger_api)),
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
