from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="OIPD API",
        default_version='',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="artnyr2004@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=[permissions.IsAdminUser],
)

api_urlpatterns = [
    path('about_us/', include('apps.about_us.urls')),
    path('categories/', include('apps.categories.urls')),
    path('contacts/', include('apps.contacts.urls')),
    path('library/', include('apps.libraries.urls')),
    path('news/', include('apps.news.urls')),
    path('our_approach/', include('apps.our_approach.urls')),
    path('partners/', include('apps.partners.urls')),
    path('socials/', include('apps.socials.urls')),
    path('team/', include('apps.team.urls')),
    path('clubs/', include('apps.club.urls')),
    path('posts/', include('apps.posts.urls')),
    path('service/', include('apps.service_texts.urls')),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),

    # docs
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
