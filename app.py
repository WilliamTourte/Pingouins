from flask import Flask, render_template, request, jsonify
from dal.dalImpl import get_all_pingouins, get_pingouin, delete_pingouin, update_pingouin

app = Flask(__name__)

@app.route('/delete_pingouin/<int:id>', methods=['DELETE'])
def delete_pingouin_route(id):
    delete_pingouin(id)
    return jsonify({'status': 'success'})

@app.route('/')
def index():
    print("Index Page")
    pingouins = get_all_pingouins()

    return render_template('accueil.html', pingouins=pingouins)


if __name__ == '__main__':
    app.run()
