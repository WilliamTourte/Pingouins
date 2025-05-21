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
        pingouin=(f"Id : {self._id} \n"
                  f"Espèce : {self._espece} \n"
                  f"Île : {self._ile} \n"
                  f"Longueur du bec : {self._bec_longueur} mm \n"
                  f"Profondeur du bec : {self._bec_profondeur} mm \n"
                  f"Longueur de la nageoire : {self._nageoire_longeur} mm \n"
                  f"Poids : {self._poids} kg\n"
                  f"Sexe : {self._sexe} \n"
                  f"Année de naissance : {self._annee_naissance}\n")



        return pingouin

