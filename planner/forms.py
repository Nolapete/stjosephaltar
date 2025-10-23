from django import forms
from .models import Route, Stop
from leaflet.forms.widgets import LeafletWidget

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name']

class StopForm(forms.ModelForm):
    class Meta:
        model = Stop
        fields = ['name', 'location', 'order']
        widgets = {
            'location': LeafletWidget(),
        }