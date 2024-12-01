# Necessary packages
# !pip install tensorflow==2.15.0 keras==2.15.0 keras-cv==0.6.0 keras-core==0.1.7 tensorflow-datasets==4.9.6

# Doc : https://keras.io/keras_hub/guides/stable_diffusion_3_in_keras_hub/

# Importation des bibliothèques nécessaires
import keras_cv  # Pour accéder aux modèles de vision par ordinateur, comme Stable Diffusion
import keras  # Bibliothèque de deep learning utilisée pour créer et entraîner des modèles
import matplotlib.pyplot as plt  # Pour visualiser les images générées
import time  # Pour mesurer le temps d'exécution si nécessaire (non utilisé directement ici)

# Chargement du modèle Stable Diffusion de Keras
# img_width et img_height : dimensions des images générées (512x512 pixels ici).
# jit_compile=True : optimise les performances en compilant les opérations en JIT (Just-In-Time).
model = keras_cv.models.StableDiffusion(
    img_width=512, img_height=512, jit_compile=True
)

# Génération d'images à partir d'une description textuelle
# 'a flying man' : la description utilisée comme prompt pour générer l'image.
# batch_size=1 : génère une seule image pour ce prompt.
images = model.text_to_image('a flying man', batch_size=1)

# Fonction pour afficher les images générées
def plot_images(images):
    plt.figure(figsize=(20, 20))  # Taille de la figure pour afficher les images
    for i in range(len(images)):  # Parcourt toutes les images dans la liste
        ax = plt.subplot(1, len(images), i + 1)  # Création d'une sous-figure pour chaque image
        plt.imshow(images[i])  # Affiche l'image
        plt.axis("off")  # Supprime les axes pour une visualisation propre

# Appel de la fonction pour afficher l'image générée
plot_images(images)


'''
Explication globale :

    1. Modèle Stable Diffusion : Le modèle est configuré pour générer des images à partir de descriptions textuelles.
    2. Prompt textuel : Le texte "a flying man" est utilisé comme input pour décrire l'image à générer.
    3. Image générée : Une image de taille 512×512512×512 est créée par le modèle.
    4. Visualisation : La fonction plot_images affiche l'image générée dans une fenêtre graphique avec matplotlib.
'''
