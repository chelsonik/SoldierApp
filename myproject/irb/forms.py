from django import forms

place_choice =(
    ("Przepustka", "Przepustka"),
    ("Obecny", "Obecny"),
    ("L4", "L4"),
)

class Presenceform(forms.Form):
    soldier_id = forms.CharField(label='Nr ksiazeczki')
    name = forms.CharField(label='Imie i nazwisko')
    place = forms.ChoiceField(label='Obecny', choices=place_choice)
    date_w = forms.DateField(label='Data wyjazdu', required=False)
    date_p = forms.DateField(label='Data powrotu', required=False)
    stay = forms.CharField(label='Miejsce pobytu', required=False)

