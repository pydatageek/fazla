from django.conf import settings
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

handler400 = 'sections.views.handler400'
handler403 = 'sections.views.handler403'
handler404 = 'sections.views.handler404'
handler500 = 'sections.views.handler500'

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
