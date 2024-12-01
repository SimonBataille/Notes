# Importation des modules nécessaires
from keras.models import Sequential  # Pour créer un modèle de réseau de neurones séquentiel
from keras import layers  # Contient des types de couches comme Dense, Convolutional, etc.
import numpy as np  # Utilisé pour manipuler des données sous forme de tableaux (arrays)

# Définir le modèle séquentiel
model = Sequential()  # Initialise un modèle où les couches seront empilées les unes après les autres

# Ajout de la première couche (couche dense avec 3 neurones et une entrée scalaire)
model.add(layers.Dense(units=3, input_shape=[1]))  
# - units=3 : cette couche contient 3 neurones
# - input_shape=[1] : chaque entrée est un scalaire (dimension 1)

# Ajout de trois couches cachées supplémentaires, chacune contenant 64 neurones
model.add(layers.Dense(units=64))  # Une couche dense avec 64 neurones
model.add(layers.Dense(units=64))  # Une autre couche dense avec 64 neurones
model.add(layers.Dense(units=64))  # Encore une autre couche dense avec 64 neurones
# Les couches cachées traitent les informations de manière non linéaire grâce à leurs activations par défaut (ReLU).

# Ajout d'une couche finale avec un seul neurone
model.add(layers.Dense(units=1))  
# - units=1 : cette couche produit une sortie scalaire, adaptée à un problème de régression (prédire un nombre)

# Définir les données d'entrée et de sortie pour entraîner le modèle
entree = np.array([1, 2, 3, 4, 5], dtype=float)  # Entrées : un tableau NumPy contenant des nombres
sortie = np.array([2, 4, 6, 8, 10], dtype=float)  # Sorties : chaque sortie est égale à 2 fois l'entrée
# Exemple : si l'entrée est 3, la sortie correspondante est 6.

# Compiler le modèle (préparation pour l'entraînement)
model.compile(
    loss='mean_squared_error',  # Fonction de perte utilisée pour mesurer l'écart entre les prédictions et les vraies valeurs
    optimizer='adam'  # Algorithme d'optimisation Adam pour ajuster les poids du modèle
)

# Entraîner le modèle avec les données
model.fit(
    x=entree,  # Données d'entrée (features)
    y=sortie,  # Données de sortie (labels)
    epochs=100  # Nombre d'itérations (passages sur les données d'entraînement)
)
# Le modèle apprend à prédire la relation y = 2x à partir des données fournies.

# Boucle interactive pour tester le modèle avec de nouvelles entrées
while True:  # Crée une boucle infinie pour permettre des prédictions répétées
    x = float(input('Nombre : '))  # Demande à l'utilisateur d'entrer un nombre (converti en float)
    prediction = model.predict(np.array([x], dtype=float))  
    # Convertit l'entrée utilisateur en tableau NumPy et fait une prédiction
    # `np.array([x])` : transforme l'entrée en une forme compatible avec le modèle
    print('Prediction : ' + str(prediction[0][0]))  
    # Affiche la prédiction. La sortie est un tableau 2D, donc on accède au premier élément avec [0][0].

# Exemple attendu après entraînement :
# Si l'utilisateur entre "3", le modèle devrait prédire "6" (ou un nombre proche).


'''
Points importants

    1. Structure du modèle :
        1 couche d'entrée (3 neurones),
        plusieurs couches cachées (64 neurones chacune),
        1 couche de sortie (1 neurone).

    2. Fonctionnement :
        Le modèle apprend une relation linéaire simple (y = 2x) entre l'entrée et la sortie.
        Les couches supplémentaires ajoutent de la capacité au réseau mais sont excessives pour un problème aussi simple.

    3. Optimisation :
        adam est utilisé pour ajuster les poids efficacement, même pour des problèmes non linéaires.

    4. Prédiction :
        Le modèle utilise les poids appris pour estimer la sortie correspondant à une nouvelle entrée fournie par l'utilisateur.

Ce code est un exemple de base pour montrer comment utiliser un réseau de neurones pour modéliser une fonction simple.
''''





