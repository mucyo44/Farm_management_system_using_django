from django import forms
from .models import Records

class LivestockForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['animal_type', 'birth_date', 'status','date']




    