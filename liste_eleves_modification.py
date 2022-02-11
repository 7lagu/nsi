
# -*- coding: utf-8 -*-
"""
Created on sunday Dec  12 18:55:37 2021

@author: TitouanDENIS
"""

import pandas
import random
from random import choice
import string



#on importe le fichier csv sous le nom de 'liste' avec le module pandas
liste = pandas.read_csv("liste_eleves.csv")


# On génère le nom d'utilisateur 

for ligne in range (len(liste)):
    # variables : pn = prénom nm = nom user = username final
    pn = liste.loc[ligne, 'prenom'][0] #on ne récupère que la 1ere lettre du prenom
    pn = pn.lower()
    nm = liste.loc[ligne, 'nom']
    nm = nm.lower()
    #on forme e nom d'utilisateur à partir du nom et prénom
    user = pn + nm 
    
    # on enregistre le nom d'utilisateur dans une nouvelle colonne
    # "Username" de la DataFrame
    liste.loc[ligne, 'Utilisateurs'] = user



# On génère le mot de passe
    
for ligne in range(len(liste)):
    # mdp = mot de passe valeurs = valeurs à choisir au hasard pour le mot de passe
    mdp = ""
    # on utilise les listes du module string pour définir les caractères possibles dans la fonction choice
    valeurs = string.ascii_lowercase + string.digits
    
    # on utilise la fonction choice du module random pour choisir
    # 8 fois des caractères aux hasard depuis la liste 'valeurs'
    
    for i in range(8):
            mdp = mdp + (choice(valeurs))
            
    # on enregistre le mot de passe dans une nouvelle colonne
    # "Mot de passe" de la DataFrame
    liste.loc[ligne, 'Mot de passe'] = mdp
    
print(liste)

#on enregistre la DataFrame 'liste' importée au début en tant que liste_finale.csv 

liste.to_csv("liste_finale2.csv")



    

