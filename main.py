#qst4
from noeud import Noeud
#qst 6
import numpy as np

# Les feuilles
n2 = Noeud(2, [])
ny = Noeud("y", [])

# Le + : 2 + y
somme = Noeud("+", [n2, ny])
# Le exp : exp(2 + y)
nexp = Noeud("exp", [somme])

print(nexp.affichage_polonais())
#qst5
print(nexp.evaluer({"y": 3}))
#qst6
valeurs = {
    "y": np.linspace(-10, 10, 100)
}

somme.tracer(valeurs, "y")