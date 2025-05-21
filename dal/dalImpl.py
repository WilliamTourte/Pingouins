import pymssql
from modele import pingouin
IP='127.0.0.1'
SERVER = 'localhost'
USER = 'SA'
PWD = 'P@$$word'
BDD = 'PINGOUINS'

def __repr__(self):
    return str(self)

#Créez une méthode get_all_pingouins()
# #Elle doit renvoyer une liste de pingouins en utilisant la classe Pingouin précédemment créée
def get_all_pingouins():
     liste=[]
     with pymssql.connect(SERVER, USER, PWD, BDD) as conn:
        with conn.cursor(as_dict=True) as cursor:
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

#Supprime le pingouin dont on donne l'id
def delete_pingouin(id_pingouin):

    with pymssql.connect(SERVER, USER, PWD, BDD) as conn:
        with conn.cursor(as_dict=True) as cursor:
            id_pingouin=str(id_pingouin)
            cursor.execute(""" CREATE PROCEDURE DeletePingouin @id VARCHAR(3)
            AS
            BEGIN
                SELECT *
                FROM Pingouins
                WHERE id_pingouin like @id
            END """)
            cursor.callproc('DeletePingouin', (id_pingouin,))
            for row in cursor:
                print(row)



delete_pingouin("10")

'''Liste=get_all_pingouins()
for pingouin in Liste:
    print(pingouin)'''

