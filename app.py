from flask import Flask, render_template
from dal.dalImpl import get_all_pingouins, get_pingouin, delete_pingouin, update_pingouin

app = Flask(__name__)


@app.route('/')
def index():
    print("Index Page")
    pingouins = get_all_pingouins()
    print(pingouins)
    return render_template('accueil.html', pingouins=pingouins)


if __name__ == '__main__':
    app.run()
