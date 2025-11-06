from django.urls import path

from .views import RouteCreateView, RouteDetailView, RouteListView, add_stop_to_route

app_name = "planner"

urlpatterns = [
    path("", RouteListView.as_view(), name="route_list"),
    path("new/", RouteCreateView.as_view(), name="route_create"),
    path("<int:pk>/", RouteDetailView.as_view(), name="route_detail"),
    path("<int:pk>/add_stop/", add_stop_to_route, name="add_stop_to_route"),
]
