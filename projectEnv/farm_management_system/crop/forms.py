from django import forms
from .models import Crop


class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name','planting_date','harvest_date','yield_amount','season']