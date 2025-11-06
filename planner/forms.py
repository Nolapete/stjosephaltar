from django import forms
from leaflet.forms.widgets import LeafletWidget

from .models import Route, Stop


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ["name"]


class StopForm(forms.ModelForm):
    class Meta:
        model = Stop
        fields = ["name", "location", "order"]
        widgets = {
            "location": LeafletWidget(),
        }
