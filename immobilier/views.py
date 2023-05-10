from django.shortcuts import render


# Create your views here.
def page_accueil(request):
    return render(request, 'page_accueil.html')

def location(request):
    return render(request, 'location.html')

def vente(request):
    return render(request, 'vente.html')

def renovation(request):
    return render(request, 'renovation.html')
