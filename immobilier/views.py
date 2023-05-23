from django.shortcuts import render
from .models import Article, Newsletter
from .forms import FormulaireNewsletter


# Create your views here.
def page_accueil(request):
    form=FormulaireNewsletter()
    if request.method=='POST':
        form= FormulaireNewsletter(request.POST)
        if form .is_valid():
            form.save()
    return render(request, 'page_accueil.html')

def location(request):
    return render(request, 'location.html')

def vente(request):
    return render(request, 'vente.html')

def renovation(request):
    return render(request, 'renovation.html')

def liste_article(request):

    tous_les_articles= Article.objects.all()
    return render(request, 'liste_article.html', locals())



def détail_article(request, pk):
    article= Article.objects.get(id=pk)
    return render(request, 'détail_article.html', locals())



