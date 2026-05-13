from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_cours, name='liste_cours'),
    
    path('ajouter/', views.ajouter_cours, name='ajouter_cours'),
    
    path('modifier/<int:cours_id>/', views.modifier_cours, name='modifier_cours'),

path('supprimer/<int:cours_id>/', views.supprimer_cours, name='supprimer_cours'),

path('detail/<int:cours_id>/', views.detail_cours, name='detail_cours'),
]