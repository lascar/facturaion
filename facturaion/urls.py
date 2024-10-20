from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns

admin.site.site_header = "facturaion"
admin.site.site_title = "facturaion"
admin.site.index_title = "facturaion Admin"

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('factu/', include('factu.urls')),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('i18n/', include('django.conf.urls.i18n')),
]
