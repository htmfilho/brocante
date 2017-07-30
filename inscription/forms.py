from django import forms
from inscription.models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        exclude = ['registered', 'status']
