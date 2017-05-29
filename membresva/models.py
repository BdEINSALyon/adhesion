"""
Modèle du membre VA
"""
from django.db import models

class Membre(models):
    
    NOM =  models.CharField(max_length=70)
    PRENOM = models.CharField(max_length=70)
    HOMME = models.BooleanField()
    DATENAISSANCE = models.DateField()
    TEL = models.IntegerField()
    DONNEES MEDICALES = models.TextField()
    INFOS = models.TextField()
    MAIL = models.Charfield(max_length=200)
    DEPT = models.ForeignKey('Depart')
    ANNEE = models.ForeignKey('Annee')
    #L'ID de la carte VA de l'étudiant
    IDVA = models.IntegerField()
    #L'ID de la carte étudiant 
    IDETU = models.IntegerField()

    def __str__(self):
        return self.nom + "  " + self.prenom


class Depart(models):
    NOM = models.CharField(max_length=100)
    ABBREVIATION = models.CharField(max_lenght=6)
    ACTIF = models.BooleanField()

    def __str__(self):
        return self.nom

class Annee(models):
    NOM = models.CharField(max_length=100)
    ORDRE = models.IntegerField()
    ACTIF = models.BooleanField()

    def __str__(self):
        return self.nom
