from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm

# views.

def contacte(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Traitez les données du formulaire ici
            form.save()
            # Redirigez vers une autre vue ou affichez un message de confirmation
            return HttpResponse("Formulaire enregistré avec succès.")
    else:
        form = ContactForm()

    # Si le formulaire a été soumis avec succès, affichez un message de confirmation
    submitted = request.GET.get('submitted', False)

    return render(request, 'hello/contacte.html', {'form': form, 'submitted': submitted})

def index(request):
    return HttpResponse("hello!!!!!!!")

def epicerie(request):
    return render(request, "hello/epicerie.html")

def boulangerie(request):
    return render(request, "hello/boulangerie.html")

def efrigo(request):
    return render(request, "hello/e-frigo.html")

def casiers(request):
    return render(request, "hello/casiers.html")


