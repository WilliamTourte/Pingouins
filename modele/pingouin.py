class Pingouin:
    def __init__(self, *args):
        # Vérifiez que le nombre d'arguments est correct
        if len(args) == 1 and isinstance(args[0], list):
            # Si un seul argument est fourni et que c'est une liste, utilisez-la
            attrs = args[0]
            if len(attrs) != 9:
                raise ValueError("La liste doit contenir exactement 9 éléments.")
            self._id = attrs[0]
            self._espece = attrs[1]
            self._ile = attrs[2]
            self._bec_longueur = attrs[3]
            self._bec_profondeur = attrs[4]
            self._nageoire_longueur = attrs[5]
            self._poids = attrs[6]
            self._sexe = attrs[7]
            self._annee_naissance = attrs[8]
        else:
            # Sinon, utilisez les arguments positionnels
            if len(args) != 9:
                raise ValueError("Le constructeur attend 9 arguments ou une liste de 9 éléments.")
            self._id = args[0]
            self._espece = args[1]
            self._ile = args[2]
            self._bec_longueur = args[3]
            self._bec_profondeur = args[4]
            self._nageoire_longueur = args[5]
            self._poids = args[6]
            self._sexe = args[7]
            self._annee_naissance = args[8]


    def __str__(self):
        pingouin=(f"Id : {self._id} \n"
                  f"Espèce : {self._espece} \n"
                  f"Île : {self._ile} \n"
                  f"Longueur du bec : {self._bec_longueur} mm \n"
                  f"Profondeur du bec : {self._bec_profondeur} mm \n"
                  f"Longueur de la nageoire : {self._nageoire_longueur} mm \n"
                  f"Poids : {self._poids} kg\n"
                  f"Sexe : {self._sexe} \n"
                  f"Année de naissance : {self._annee_naissance}\n")
        return pingouin

    def get_attributs(self):
        return {attr: value for attr, value in vars(self).items()}
'''def __init__(self, id, espece, ile, bec_longueur, bec_profondeur, nageoire_longeur, poids, sexe, annee_naissance):'''
'''self._id = id
self._espece = espece
self._ile = ile
self._bec_longueur = bec_longueur
self._bec_profondeur = bec_profondeur
self._nageoire_longueur = nageoire_longeur
self._poids = poids
self._sexe = sexe
self._annee_naissance = annee_naissance'''