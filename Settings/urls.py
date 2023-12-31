from django.contrib import admin
from django.urls import path, include
from rest_framework import routers,permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
router = routers.SimpleRouter()
schema_view = get_schema_view(
    openapi.Info(
        title="API documention",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.pigs.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
]