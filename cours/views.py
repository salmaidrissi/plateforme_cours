from django.shortcuts import render
from .models import Cours

def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/liste.html', {'cours': cours})
