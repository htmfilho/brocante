from django import forms
from inscription.models import inscription


class InscriptionForm(forms.ModelForm):
    class Meta:
        model = inscription.Inscription
        exclude = ['registered', 'status']
