import mysql.connector as msql

bdd = None
cursor = None

def connexion():
    global bdd
    global cursor

    bdd = msql.connect(user='root', password='root', host='localhost', port="8081", database='promesse_dons')
    cursor = bdd.cursor()
    
def deconnexion():
    global bdd
    global cursor

    cursor.close()
    bdd.close()

def get_users() :
    global cursor

    connexion()
    query = "SELECT * FROM utilisateur"
    cursor.execute(query)
    utilisateurs = []

    for enregistrement in cursor :
        utilisateur = {}
        utilisateur['id_utilisateur'] = enregistrement[0]
        utilisateur['nom'] = enregistrement[1]
        utilisateur['prenom'] = enregistrement[2]
        utilisateur['email'] = enregistrement[3]
        utilisateur['adresse'] = enregistrement[4]
        utilisateur['don'] = enregistrement[5]
        
        utilisateurs.append(utilisateur)
   
    print(utilisateurs)
    deconnexion()
    return utilisateurs

def somme():
    connexion()
    total=0
    query="SELECT * FROM utilisateur"
    cursor.execute(query)
    for enregistrement in cursor:
        total +=enregistrement[5]
    deconnexion()
    return (total)

# récupèrer infos + ajout dans bdd ('promesse_dons')
def set_utilisateur(nom,prenom,email,adresse,don): 
    global bdd
    global cursor

    connexion()

    query="INSERT INTO utilisateur(nom,prenom,email,adresse,don) VALUES ('"+nom+"','"+prenom+"','"+email+"','"+adresse+"','"+don+"')"
    cursor.execute(query)
    bdd.commit()



    deconnexion()
 

# def set_utilisateur(nom, prenom, naissance):
#     global bdd
#     global cursor

#     connexion()

#     query="INSERT INTO utilisateurs(nom, prenom, email, adresse, don) VALUES ('"+nom+"','"+prenom+"','"+e-mail+"', '"+adresse+"', '"don"')"
#     cursor.execute(query)
#     bdd.commit()

#     deconnexion()


#     # verifier nom, prenom = valeurs exactes
