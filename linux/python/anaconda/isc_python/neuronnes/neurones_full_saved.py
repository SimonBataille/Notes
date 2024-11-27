from keras.models import Sequential, load_model
from keras import layers
import numpy as np
import os

# Chemin du fichier de sauvegarde du modèle
model_path = "mon_modele.h5"

if os.path.exists(model_path):
    # Charger le modèle si le fichier existe
    model = load_model(model_path)
    print("Modèle chargé depuis le fichier.")
else:
    # Créer et entraîner le modèle si le fichier n'existe pas
    model = Sequential()
    model.add(layers.Dense(units=3, input_shape=[1]))
    model.add(layers.Dense(units=64))
    model.add(layers.Dense(units=1))

    # Données d'entraînement
    entree = np.array([1, 2, 3, 4, 5], dtype=float)
    sortie = np.array([2, 4, 6, 8, 10], dtype=float)

    # Compiler et entraîner le modèle
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x=entree, y=sortie, epochs=100)

    # Sauvegarder le modèle après l'entraînement
    model.save(model_path)
    print("Modèle entraîné et sauvegardé.")

# Utilisation du modèle pour les prédictions
while True:
    x = float(input('Nombre : '))
    prediction = model.predict(np.array([x], dtype=float))
    print('Prédiction : ' + str(prediction[0][0]))

