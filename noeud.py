#qst5
import math
#qst6
import matplotlib.pyplot as plt
import numpy as np

class Noeud:

    def __init__(self, valeur, enfants):
        self.valeur = valeur
        self.enfants = enfants

#qst2
    def ajouter_enfant(self, enfant):
        self.enfants.append(enfant)
#qst 3
    def affichage_polonais(self):
        resultat = str(self.valeur)

        for enfant in self.enfants:
            resultat += " " + enfant.affichage_polonais()

        return resultat
#qst5 
    def evaluer (self,valeurs):#self :reprend le noeud actiel ,valeur: contient les val des variables
        #si la valeur est un nbr
        if isinstance(self.valeur, (int, float)):
            return float(self.valeur) #si le noeud contien 2 on obtient 2.0
        #si c une variable
        #cette ligne demande Est-ce que la valeur du nœud n'est pas un opérateur ?
        if self.valeur not in ["+", "-", "*", "/", "exp", "log", "sin", "cos"]:
            if self.valeur not in valeurs:
                raise ValueError("Variable non définie")#Arrête le programme et indique qu'une variable n'a pas été définie
            return float(valeurs[self.valeur])

        # On évalue les enfants
        valeurs_enfants = []#on cree une liste vide car on va y mettre  la val de chaque enfant
        for enfant in self.enfants:
            valeurs_enfants.append(enfant.evaluer(valeurs))

        # Opérations
        if self.valeur == "+":
            return valeurs_enfants[0] + valeurs_enfants[1]

        if self.valeur == "-":
            return valeurs_enfants[0] - valeurs_enfants[1]

        if self.valeur == "*":
            return valeurs_enfants[0] * valeurs_enfants[1]

#facultatif
        if self.valeur == "/":
            return valeurs_enfants[0] / valeurs_enfants[1]

        if self.valeur == "exp":
            return math.exp(valeurs_enfants[0])

        if self.valeur == "log":
            return math.log(valeurs_enfants[0])

        if self.valeur == "sin":
            return math.sin(valeurs_enfants[0])

        if self.valeur == "cos":
            return math.cos(valeurs_enfants[0])



#qst6
    # Q6
    def tracer(self, valeurs, variable):

        x = valeurs[variable]

        y = []

        for valeur in x:
            valeurs[variable] = valeur
            y.append(self.evaluer(valeurs))

        plt.plot(x, y)
        plt.xlabel(variable)
        plt.ylabel("f(" + variable + ")")
        plt.grid()
        plt.show()