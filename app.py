from flask import Flask, render_template, request, redirect, url_for, flash

from dal.dalImpl import get_pingouin, get_all_pingouins, update_pingouin, delete_pingouin
from modele.pingouin import Pingouin

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'  # Nécessaire pour utiliser flash

# Exemple de fonction pour mettre à jour un pingouin dans la base de données
def update_pingouin_in_db(id, espece, ile, longueur_bec, profondeur_bec, longueur_nageoire, poids, sexe, annee_naissance):
    print(f"Mise à jour du pingouin avec l'ID : {id}")
    # Ajoutez ici la logique pour mettre à jour le pingouin dans la base de données
    # Exemple : cursor.execute("UPDATE Pingouins SET espece = %s, ile = %s, ... WHERE id_pingouin = %s", (espece, ile, ..., id))

@app.route('/update_pingouin/<int:id>', methods=['GET', 'POST'])
def update_pingouin_route(id):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        espece = request.form['espece']
        ile = request.form['ile']
        longueur_bec = request.form['longueur_bec']
        profondeur_bec = request.form['profondeur_bec']
        longueur_nageoire = request.form['longueur_nageoire']
        poids = request.form['poids']
        sexe = request.form['sexe']
        annee_naissance = request.form['annee_naissance']

        # Mettre à jour le pingouin dans la base de données
        pingouinmodifie = Pingouin(id, espece, ile, longueur_bec, profondeur_bec, longueur_nageoire, poids, sexe, annee_naissance)
        update_pingouin(pingouinmodifie)

        # Ajouter un message flash pour confirmer la mise à jour
        flash('Les informations du pingouin ont été mises à jour avec succès.', 'success')

        # Rediriger vers la page d'accueil
        return redirect(url_for('index'))
    else:
        # Récupérer les informations du pingouin
        pingouin = get_pingouin(id)
        if pingouin:
            return render_template('modification.html', pingouin=pingouin)
        else:
            return "Pingouin non trouvé", 404

@app.route('/')
def index():
    pingouins = get_all_pingouins()
    return render_template('accueil.html', pingouins=pingouins)

if __name__ == '__main__':
    app.run(debug=True)
