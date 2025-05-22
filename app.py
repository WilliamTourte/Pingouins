from flask import Flask, render_template, request, jsonify
from dal.dalImpl import get_all_pingouins, get_pingouin, delete_pingouin, update_pingouin

app = Flask(__name__)

@app.route('/delete_pingouin/<int:id>', methods=['DELETE'])
def delete_pingouin_route(id):
    delete_pingouin(id)
    return jsonify({'status': 'success'})


@app.route('/update_pingouin/<int:id>', methods=['GET', 'POST'])
def update_pingouin_route(id):
    if request.method == 'POST':
        # Logique pour mettre à jour le pingouin dans la base de données
        update_pingouin(id)
        return jsonify({"status": "success"})
    else:
        # Récupérer les informations du pingouin
        pingouin = get_pingouin(id)
        if pingouin:
            return render_template('modification.html', pingouin=pingouin)
        else:
            return "Pingouin non trouvé", 404
@app.route('/')
def index():
    print("Index Page")
    pingouins = get_all_pingouins()

    return render_template('accueil.html', pingouins=pingouins)


if __name__ == '__main__':
    app.run()
