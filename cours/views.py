<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
=======
from django.shortcuts import render
from .models import Cours
from .forms import CoursForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q
>>>>>>> b35346c69ed704878ac5e371fe0534b559a8d985

from .models import Cours, Inscription, Profile


# =========================
# LISTE DES COURS
# =========================
def liste_cours(request):
<<<<<<< HEAD
    cours = Cours.objects.all()
    return render(request, 'liste.html', {'cours': cours})


# =========================
# REGISTER
# =========================
def register_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Profile.objects.create(user=user, role=role)

        return redirect('login')

    return render(request, 'register.html')


# =========================
# LOGIN
# =========================
def login_view(request):

    error = ''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('liste_cours')
        else:
            error = "Nom d'utilisateur ou mot de passe incorrect"

    return render(request, 'login.html', {'error': error})


# =========================
# LOGOUT
# =========================
def logout_view(request):
    logout(request)
    return redirect('login')


# =========================
# INSCRIPTION COURS
# =========================
@login_required
def inscrire_cours(request, cours_id):

    cours = get_object_or_404(Cours, id=cours_id)

    existe = Inscription.objects.filter(
        etudiant=request.user,
        cours=cours
    ).exists()

    if not existe:
        Inscription.objects.create(
            etudiant=request.user,
            cours=cours
        )

    return redirect('liste_cours')


# =========================
# MES COURS (DASHBOARD ETUDIANT)
# =========================
@login_required
def mes_cours(request):

    inscriptions = Inscription.objects.filter(etudiant=request.user)

    return render(request, 'mes_cours.html', {
        'inscriptions': inscriptions
=======
    query = request.GET.get('q')

    if query:
        cours = Cours.objects.filter(
            Q(titre__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        cours = Cours.objects.all()

    return render(request, 'cours/liste.html', {
        'cours': cours,
        'query': query
    })

def ajouter_cours(request):

    if request.method == 'POST':

        form = CoursForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            cours = form.save(commit=False)

            cours.enseignant = User.objects.first()

            cours.save()

            return redirect('liste_cours')

    else:

        form = CoursForm()

    return render(
        request,
        'cours/ajouter.html',
        {'form': form}
    )
def modifier_cours(request, cours_id):

    cours = get_object_or_404(Cours, id=cours_id)

    if request.method == 'POST':

        form = CoursForm(
            request.POST,
            request.FILES,
            instance=cours
        )

        if form.is_valid():

            form.save()

            return redirect('liste_cours')

    else:

        form = CoursForm(instance=cours)

    return render(
        request,
        'cours/modifier.html',
        {'form': form}
    )

def supprimer_cours(request, cours_id):

    cours = get_object_or_404(Cours, id=cours_id)

    cours.delete()

    return redirect('liste_cours')

def detail_cours(request, cours_id):

    cours = get_object_or_404(Cours, id=cours_id)

    return render(request, 'cours/detail.html', {'cours': cours})

def dashboard_enseignant(request):
    cours = Cours.objects.filter(enseignant=User.objects.first())

    return render(request, 'cours/dashboard_enseignant.html', {
        'cours': cours
>>>>>>> b35346c69ed704878ac5e371fe0534b559a8d985
    })