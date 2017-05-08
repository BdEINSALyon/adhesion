"""
Modèle du membre VA
"""
from django.db import models

class Membre(models):
    nom =  models.CharField(max_length=70)
    prenom = models.CharField(max_length=70)
    homme = models.BooleanField()
    datenaissance = models.DateField()
    tel = models.IntegerField()
    infos = models.TextField()
    mail = models.Charfield(max_length=200)
    dept = models.ForeignKey('Depart')
    annee = models.IntegerField()
    IDVA = models.IntegerField()
    IDETU = models.IntegerField()
    estmembre = models.BooleanField()
    adhesions = models.CharField(max_length=300)

    def __str__(self):
        return self.nom + "  " + self.prenom


class Depart(models):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom