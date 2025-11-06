from django.urls import path

from . import views

app_name = "altars"

urlpatterns = [
    path("add/", views.add_altar, name="add_altar"),
    path("", views.list_altars, name="list_altars"),
    path("update/<int:altar_id>/", views.update_altar, name="update_altar"),
    path("delete/<int:altar_id>/", views.delete_altar, name="delete_altar"),
    path("search/", views.search_altars, name="search_altars"),
    path("find/", views.find_altars_view, name="find_altars"),
    path("details/<int:altar_id>/", views.altar_details, name="altar_details"),
]
