from django import forms
from .models import Kniha

class KnihaForm(forms.ModelForm):

    class Meta:
        model = Kniha
        fields=["nazev", "autor", "zanr"]