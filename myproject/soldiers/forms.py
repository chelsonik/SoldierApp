from django import forms

from .models import Soldier

class Soldierform(forms.ModelForm):
    class Meta:
        model = Soldier
        fields = [
            'name',
            'surname',
            'reason',
            'platoon'
        ]

class RawSoldierForm(forms.Form):
    name    = forms.CharField()
    surname = forms.CharField()
    reason =  forms.CharField()
    platoon = forms.IntegerField()