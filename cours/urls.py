from django.urls import path
from .views import mes_cours

from .views import (
    liste_cours,
    register_view,
    login_view,
    logout_view,
    inscrire_cours
)

urlpatterns = [
<<<<<<< HEAD
    path('', liste_cours, name='liste_cours'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('inscrire/<int:cours_id>/', inscrire_cours, name='inscrire_cours'),
    path('mes-cours/', mes_cours, name='mes_cours'),
=======
    path('', views.liste_cours, name='liste_cours'),
    
    path('dashboard-enseignant/', views.dashboard_enseignant, name='dashboard_enseignant'),
    
    path('ajouter/', views.ajouter_cours, name='ajouter_cours'),
    
    path('modifier/<int:cours_id>/', views.modifier_cours, name='modifier_cours'),

path('supprimer/<int:cours_id>/', views.supprimer_cours, name='supprimer_cours'),

path('detail/<int:cours_id>/', views.detail_cours, name='detail_cours'),

>>>>>>> b35346c69ed704878ac5e371fe0534b559a8d985
]