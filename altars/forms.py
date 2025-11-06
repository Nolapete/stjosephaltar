from django import forms

from .models import Altar


class AltarForm(forms.ModelForm):
    class Meta:
        model = Altar
        fields = [
            "name",
            "location",
            "address1",
            "address2",
            "address3",
            "city",
            "state",
            "zipcode",
            "established_date",
        ]
