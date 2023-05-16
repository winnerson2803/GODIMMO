from django.contrib import admin
from django.urls import path, include
from . import views
from .views import page_accueil, location, vente, renovation, liste_article, détail_article
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.page_accueil , name='page_accueil'),
    path('location/', views.location, name='location'),
    path('vente/', views.vente, name='vente'),
    path('renovation/', views.renovation, name='renovation'),
    path('liste_article/', views.liste_article, name='liste_article'),
    path('détail_article/<int:pk>', views.détail_article, name='detail_article'),


]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)