from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path


urlpatterns = [
    path('adminp/', admin.site.urls),
    # path('sitemap.xml', sitemap, {'sitemaps': ''},
    #      name='django.contrib.sitemaps.views.sitemap'),

    path('', include('sections.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns \
      + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
