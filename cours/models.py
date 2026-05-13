from django.db import models
from django.contrib.auth.models import User


class Cours(models.Model):

    titre = models.CharField(max_length=200)

    description = models.TextField()
    
    pdf = models.FileField(
    upload_to='cours_pdfs/',
    null=True,
    blank=True
)
    image = models.ImageField(
        upload_to='cours_images/',
        null=True,
        blank=True
    )



    enseignant = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titre


class Inscription(models.Model):

    etudiant = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    cours = models.ForeignKey(
        Cours,
        on_delete=models.CASCADE
    )

    date_inscription = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.etudiant.username} - {self.cours.titre}"