from django.shortcuts import render
from inscription.forms import InscriptionForm

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            number_places = form.cleaned_data['number_places']
            desired_place = form.cleaned_data['desired_place']
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', locals())    
