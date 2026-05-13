from django import forms
from .models import Cours

class CoursForm(forms.ModelForm):

    class Meta:
        model = Cours
        fields = ['titre', 'description']