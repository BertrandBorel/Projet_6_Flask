from flask import Flask, render_template, request
import data

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

#  test :
@app.route('/')
def index() :
    # datas = data.get_users()
    # return render_template('index.html', utilisateurs = datas)
    return render_template('index.html')


# page de dons = formulaire
@app.route('/don')
def don():
    return render_template('formulaire.html')

# page de remerciments (message)
# @app.route('/message')
# def message():
#     return render_template('message.html')



#ajout d'un donateur à la liste
@app.route('/add', methods=['GET'])
def add():
    nom = request.values.get('nom')
    prenom = request.values.get('prenom')
    email=request.values.get('email')
    adresse=request.values.get('adresse')
    don=request.values.get('don')

    data.set_utilisateur(nom,prenom,email,adresse,don)

    datas = data.get_users()

    total=data.somme()

    return render_template('add.html', utilisateurs = datas, total=total)

if __name__ == "__main__":
    app.run(debug=True)