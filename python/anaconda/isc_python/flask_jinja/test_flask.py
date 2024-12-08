'''
conda install anaconda::flask
'''

from flask import Flask, request

app = Flask('ISC')

# on cree les routes et les fonctions associees
@app.route('/')
def bonjour():
    return '<h1>ROOT</h1>'

@app.route('/bonjour')
def bonjour_params():
    nom = request.args.get('nom', 'Tout le monde')
    return '<h1>BONJOUR ' + nom + '</h1>'

app.run()
