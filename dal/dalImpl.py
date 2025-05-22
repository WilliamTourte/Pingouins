import pymssql
from modele import pingouin
from modele.pingouin import Pingouin

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
     print("Get All Pingouins !")
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

            '''
            Création procédure DeletePingouin
            cursor.execute(""" CREATE PROCEDURE DeletePingouin @id VARCHAR(3)
            AS
            BEGIN
                DELETE
                FROM Pingouins
                WHERE id_pingouin like @id
            END """)'''
            cursor.callproc('DeletePingouin', (id_pingouin,))
            print("Supprime pingouin", id_pingouin)
            conn.commit() #Pour valider la suppression dans la base

#Met à jour le pingouin dont on donne le pingouin (instance)
def update_pingouin(pingouin):
    with pymssql.connect(SERVER, USER, PWD, BDD) as conn:
        with conn.cursor(as_dict=True) as cursor:
            id_pingouin=pingouin._id
            espece=pingouin._espece
            ile=pingouin._ile
            bec_longueur=pingouin._bec_longueur
            bec_profondeur=pingouin._bec_profondeur
            nageoire_longueur=pingouin._nageoire_longueur
            poids=pingouin._poids
            sexe=pingouin._sexe
            annee_naissance=pingouin._annee_naissance
            '''cursor.execute(""" CREATE PROCEDURE UpdatePingouin @id VARCHAR(3), @espece VARCHAR(15), @ile VARCHAR(15), @bec_l DECIMAL, @bec_p DECIMAL, @nageoire DECIMAL, @poids DECIMAL, @sexe VARCHAR(50), @annee INT
            AS
            BEGIN
                UPDATE Pingouins SET id_pingouin=@id, 
                    espece=@espece,
                    ile=@ile,
                    longueur_bec=@bec_l,
                    profondeur_bec=@bec_p,
                    longueur_nageoire=@nageoire,
                    poids=@poids,
                    sex=@sexe,
                    annee_naissance=@annee                
                WHERE id_pingouin=@id         
            END """)'''
            cursor.callproc('UpdatePingouin', (id_pingouin, espece, ile, bec_longueur, bec_profondeur, nageoire_longueur, poids, sexe, annee_naissance,))
            print("Met à jour pingouin", id_pingouin)
            conn.commit()

def  get_pingouin(id):
    with pymssql.connect(SERVER, USER, PWD, BDD) as conn:
        with conn.cursor(as_dict=True) as cursor:
            cursor.callproc('GetPingouin', (id,))
            attributs=cursor.fetchone()

            attributs_liste=[]
            for value in attributs.values():
                attributs_liste.append(value)


            pingouin=Pingouin(attributs_liste)
            return pingouin


'''Liste=get_all_pingouins()
for pingouin in Liste:
    print(pingouin)'''
'''
attributs = p.get_attributs()
for attr, value in attributs.items():
    print(f"{attr}: {value}")'''