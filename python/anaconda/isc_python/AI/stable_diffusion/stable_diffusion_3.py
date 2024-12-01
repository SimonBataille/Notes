# Installation des bibliothèques nécessaires (à décommenter si nécessaire)
# !pip install keras
# !pip install keras-hub

# Documentation de keras-hub : https://keras.io/keras_hub/guides/stable_diffusion_3_in_keras_hub/

import os  # Importation de la bibliothèque pour manipuler les variables d'environnement et les fichiers

# Spécifie le backend à utiliser pour Keras. Ici, on utilise JAX comme backend de calcul.
# Cela permet d'utiliser des opérations de calculs accélérés sur CPU ou GPU via JAX.
os.environ["KERAS_BACKEND"] = "jax"

import time  # Importation de la bibliothèque time pour mesurer le temps d'exécution (si nécessaire plus tard)

import keras  # Keras pour construire et entraîner des modèles
import keras_hub  # Keras Hub pour charger des modèles pré-entrainés (ici, Stable Diffusion 3)
import matplotlib.pyplot as plt  # Matplotlib pour afficher des graphiques et des images
import numpy as np  # Numpy pour manipuler des tableaux multidimensionnels
from PIL import Image  # PIL pour ouvrir et manipuler des images (ici, potentiellement pour sauvegarder)

# Chargement du modèle Stable Diffusion 3 à partir de Keras Hub avec les spécifications suivantes :
# - Utilisation du modèle "stable_diffusion_3_medium"
# - Taille de l'image générée : 512x512 pixels
# - Utilisation de la précision "float16" pour accélérer les calculs et réduire l'utilisation de mémoire (utile sur GPU)
text_to_image = keras_hub.models.StableDiffusion3TextToImage.from_preset(
    "stable_diffusion_3_medium", height=512, width=512, dtype="float16"
)

# Génération d'une image à partir du texte "a little flying bird"
# Cette étape utilise le modèle Stable Diffusion pour transformer la description en image
generated_image = text_to_image.generate(
    "a little flying bird"
)

# Affichage de l'image générée à l'écran avec Matplotlib
# Utilisation de plt.imshow pour afficher l'image et plt.show pour rendre l'affichage visible
plt.imshow(generated_image)
plt.axis("off")  # Masquer les axes pour une meilleure présentation de l'image
plt.show()


'''
Explications et améliorations :

    Installation des packages : Les lignes d'installation !pip install keras et !pip install keras-hub sont commentées car elles ne sont nécessaires que lors de la première installation des bibliothèques. Tu peux les décommenter si tu n'as pas encore installé ces bibliothèques dans ton environnement.

    Backend de Keras : os.environ["KERAS_BACKEND"] = "jax" définit le backend de calcul de Keras pour utiliser JAX, un framework optimisé pour les calculs sur CPU et GPU. Cela peut améliorer la vitesse d'exécution si tu travailles avec des calculs intensifs sur des modèles lourds.

    Chargement du modèle : Le modèle Stable Diffusion 3 est chargé depuis Keras Hub, qui fournit des modèles pré-entraînés pour des tâches spécifiques comme la génération d'images. Le modèle est configuré pour générer des images de 512x512 pixels avec une précision float16 pour optimiser les performances sur GPU.

    Génération de l'image : La méthode generate() prend une chaîne de texte (ici "a little flying bird") et retourne une image générée par le modèle Stable Diffusion. Cette image est stockée dans generated_image.

    Affichage de l'image : plt.imshow() permet d'afficher l'image dans un graphique, et plt.axis("off") masque les axes pour rendre l'affichage plus propre.

Notes supplémentaires :

    La première génération de l'image est plus lente car le modèle doit être chargé dans la mémoire GPU. Une fois que le modèle est chargé, les appels suivants seront plus rapides.
    Il peut être utile d'ajouter un suivi du temps d'exécution avec time.time() si tu souhaites mesurer la durée de la génération de l'image.
'''
