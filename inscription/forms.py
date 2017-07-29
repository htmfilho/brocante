from django import forms

class InscriptionForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    number_places = forms.IntegerField()
    desired_place = forms.CharField(widget=forms.Textarea, required=False)
