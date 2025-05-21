class Pingouin:
    def __init__(self, id, espece, ile, bec_longueur, bec_profondeur, nageoire_longeur, poids, sexe, annee_naissance):
        self._id = id
        self._espece = espece
        self._ile = ile
        self._bec_longueur = bec_longueur
        self._bec_profondeur = bec_profondeur
        self._nageoire_longeur = nageoire_longeur
        self._poids = poids
        self._sexe = sexe
        self._annee_naissance = annee_naissance

    def __str__(self):
        pingouin=(f"{self._id} \n"
                  f"")
        return pingouin

p=Pingouin("id","espece ","ile", "bec_longueur", "bec_profondeur", "nageoire_longueur", "poids", "sexe", "annee_naissance" )

print(p)