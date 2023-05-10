from django.contrib import admin
from django.urls import path, include
from . import views
from .views import page_accueil, location, vente, renovation


urlpatterns = [

    path('', views.page_accueil , name='page_accueil'),
    path('location/', views.location, name='location'),
    path('vente/', views.vente, name='vente'),
    path('renovation/', views.renovation, name='renovation'),
]