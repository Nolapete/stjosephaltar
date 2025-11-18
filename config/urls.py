from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views.generic import RedirectView

admin.site.site_header = "stjosephaltar.org Administration"
admin.site.site_title = "stjosephaltar.org"
admin.site.index_title = "St. Joseph Altar Admin Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landing.urls")),
    path("altars/", include("altars.urls")),
    path("accounts/", include("allauth.urls")),
    path("planner/", include("planner.urls"), name="planner"),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)),
]

if settings.DEBUG:
    import debug_toolbar
    # Append the debug toolbar URLs to the existing list
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]