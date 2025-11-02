from django.contrib import admin
from django.urls import path, include
from altars import views

admin.site.site_header = "stjosephaltar.org Administration"
admin.site.site_title = "stjosephaltar.org"
admin.site.index_title = "St. Joseph Altar Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('altars/', include('altars.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('planner/', include('planner.urls'), name='planner'),
]
