from django import forms
from .models import FarmActivity



class FarmActivityForm(forms.ModelForm):
    class Meta:
        model = FarmActivity
        fields = ['name','description','start_date','end_date']