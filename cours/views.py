from django.shortcuts import render
from .models import Cours
from .forms import CoursForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/liste.html', {'cours': cours})

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