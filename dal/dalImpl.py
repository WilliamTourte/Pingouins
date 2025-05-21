import pymssql
from modele import pingouin
IP='127.0.0.1'
SERVER = 'localhost'
USER = 'SA'
PWD = 'P@$$word'
BDD = 'PINGOUINS'

#Créez une méthode get_all_pingouins()
# #Elle doit renvoyer une liste de pingouins en utilisant la classe Pingouin précédemment créée
with pymssql.connect(SERVER, USER, PWD, BDD) as conn:
    with conn.cursor(as_dict=True) as cursor:
        def get_all_pingouins():
            liste=[]
            cursor.execute('SELECT * FROM Pingouins')
            for row in cursor.fetchall():
                id_pingouin=row['id_pingouin']
                espece=row["espece"]
                ile=row["ile"]
                bec_longueur=row["longueur_bec"]
                bec_profondeur=row["profondeur_bec"]
                nageoire_longueur=row["longueur_nageoire"]
                poids=row["poids"]
                sexe=row["sex"]
                annee_naissance=row["annee_naissance"]

                p=pingouin.Pingouin(id_pingouin,espece ,ile, bec_longueur, bec_profondeur, nageoire_longueur, poids, sexe, annee_naissance) #Construction pingouin
                liste.append(p)


            return liste



        get_all_pingouins()


