from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 
from rest_framework.permissions import AllowAny


doc_view = get_schema_view(
    openapi.Info(
        title="Bekhruz's Blog", 
        default_version = 'v1', 
        descrption = 'It`s my blog', 
        contact = openapi.Contact("Tolipov Behruz <tolipovbehruz3@gmail.com>")
    ), 
    public=True, 
    permission_classes=(AllowAny,)
)



urlpatterns = [
    path("doc/", doc_view.with_ui('swagger', cache_timeout=0), name="swagger_doc"),
    path('admin/', admin.site.urls),
    path('blog/', include('b_api.urls')),
]
