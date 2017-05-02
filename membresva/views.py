# -*- coding: utf-8 -*-
"""C'est l'application qui gère les membres de la VA. Il sont inscrit lors de l'inté ??
    
    On affichera la liste des étudiants, un descriptif de l'étudiant,...
"""


from django.http import Http404
from django.shortcuts import render


# Create your views here.
def students(request):
    
    raise Http404("Aucun étudiant trouvé !!")
    
def showstudent(request,pk):
    
    raise Http404("Aucun étudiant trouvé !")