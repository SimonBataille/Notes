from keras.models import Sequential
from keras import layers
import numpy as np
import os

# Chemin du fichier de sauvegarde des poids
weights_path = "poids_modele.weights.h5"

# Créer l'architecture du modèle
model = Sequential()
model.add(layers.Dense(units=3, input_shape=[1]))
model.add(layers.Dense(units=64))
model.add(layers.Dense(units=1))

if os.path.exists(weights_path):
    # Charger les poids si le fichier existe
    model.load_weights(weights_path)
    print("Poids chargés depuis le fichier.")
else:
    # Données d'entraînement
    entree = np.array([1, 2, 3, 4, 5], dtype=float)
    sortie = np.array([2, 4, 6, 8, 10], dtype=float)

    # Compiler et entraîner le modèle
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x=entree, y=sortie, epochs=100)

    # Sauvegarder les poids après l'entraînement
    model.save_weights(weights_path)
    print("Poids entraînés et sauvegardés.")

# Utilisation du modèle pour les prédictions
while True:
    x = float(input('Nombre : '))
    prediction = model.predict(np.array([x], dtype=float))
    print('Prédiction : ' + str(prediction[0][0]))

