from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Cours, Inscription, Profile


# =========================
# LISTE DES COURS
# =========================
def liste_cours(request):
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
    })