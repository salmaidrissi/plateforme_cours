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
    path('', liste_cours, name='liste_cours'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('inscrire/<int:cours_id>/', inscrire_cours, name='inscrire_cours'),
    path('mes-cours/', mes_cours, name='mes_cours'),
]