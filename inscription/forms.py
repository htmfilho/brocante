from django import forms

class InscriptionForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    address = forms.CharField(widget=forms.Textarea(attrs={'cols': '60', 'rows': '3'}))
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    number_places = forms.IntegerField()
    desired_place = forms.CharField(widget=forms.Textarea(attrs={'cols': '60', 'rows': '3'}),
                                    required=False)

    def __init__(self, *args, **kwargs):
        super(InscriptionForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['number_places'].widget.attrs['class'] = 'form-control'
        self.fields['desired_place'].widget.attrs['class'] = 'form-control'
