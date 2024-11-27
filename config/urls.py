from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
       title="Project API",
       default_version="v1",
       description="Project Admin API",
       terms_of_service="https://127.0.0.1:8000/",
       contact=openapi.Contact(email="admin@admin"),
       license=openapi.License(name="License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
        )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sales.urls')),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0),name="schema-swagger-ui"),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT ) 
