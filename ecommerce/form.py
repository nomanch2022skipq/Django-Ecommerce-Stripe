from django import forms

from .models import Carddata


class CardForm(forms.ModelForm):
    class Meta:
        model = Carddata
        fields = "__all__"

        widgets = {
            "expiry_date": forms.DateInput(attrs={"type": "date"}),
        }

