convert num_8.jpg -depth 8 num_8-8bit.jpg
convert num_8-8bit.jpg -channel RGB -negate output.png
conda install conda-forge::tensorflow
conda install conda-forge::keras


# Explication détaillée du code

## Importations
- `from keras.models import Sequential` : Permet de créer un modèle de réseau de neurones où les couches sont empilées de manière linéaire.
- `from keras import layers` : Fournit des types de couches standards (Dense, Convolutional, etc.).
- `import numpy as np` : Utilisé pour manipuler les données en entrée et en sortie sous forme de tableaux NumPy.

---

## Définition du modèle
- `model = Sequential()` : Initialise un modèle séquentiel, où chaque couche est ajoutée de manière successive.

### Ajout des couches
#### Première couche
- `model.add(layers.Dense(units=3, input_shape=[1]))` :
  - **`Dense`** : Une couche pleinement connectée.
  - `units=3` : Nombre de neurones dans cette couche (3 neurones).
  - `input_shape=[1]` : Chaque donnée en entrée est un scalaire (dimension 1).

#### Couches cachées
- `model.add(layers.Dense(units=64))`
- `model.add(layers.Dense(units=64))`
- `model.add(layers.Dense(units=64))`
  - Ajout de trois couches denses supplémentaires avec 64 neurones chacune.
  - Ces couches permettent d'apprendre des relations complexes grâce à leur capacité à traiter des combinaisons non linéaires des entrées.

#### Couche de sortie
- `model.add(layers.Dense(units=1))` :
  - Une couche finale avec un seul neurone.
  - Adaptée pour un problème de régression où la sortie est un scalaire.

---

## Données d'entrée et de sortie
- `entree = np.array([1, 2, 3, 4, 5], dtype=float)` : Données d'entrée (features).
- `sortie = np.array([2, 4, 6, 8, 10], dtype=float)` : Données de sortie (labels).
  - Relation : Chaque sortie est le double de l'entrée.

---

## Compilation du modèle
- `model.compile(loss='mean_squared_error', optimizer='adam')` :
  - **`loss='mean_squared_error'`** : Fonction de perte mesurant l'écart entre les prédictions et les valeurs réelles.
  - **`optimizer='adam'`** : Algorithme d’optimisation adaptatif pour ajuster les poids du modèle.

---

## Entraînement du modèle
- `model.fit(x=entree, y=sortie, epochs=100)` :
  - Entraîne le modèle sur les données d'entrée et de sortie.
  - **`epochs=100`** : Effectue 100 passages complets sur les données pour ajuster les poids.

---

## Prédictions interactives
- `while True` : Démarre une boucle infinie pour tester le modèle avec des données personnalisées.
- `x = float(input('Nombre : '))` : Demande à l'utilisateur d'entrer une valeur numérique.
- `prediction = model.predict(np.array([x], dtype=float))` :
  - Convertit l'entrée utilisateur en tableau NumPy et effectue une prédiction.
- `print('Prediction : ' + str(prediction[0][0]))` :
  - Affiche la prédiction (un scalaire attendu).

