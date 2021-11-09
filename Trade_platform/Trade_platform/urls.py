from django.urls import path, re_path, include

from rest_framework import permissions

from Traiding.urls import router

from drf_yasg.views import get_schema_view

from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Trade Platform API",
        default_version='v1',
        description="Platform for trading ",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]