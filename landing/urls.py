from django.urls import path

from . import views

app_name = "landing"

urlpatterns = [
    path("", views.index, name="landing_page"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("tradition/", views.tradition, name="tradition"),
    path("figma/", views.landing_view, name="figma_landing"),
]
