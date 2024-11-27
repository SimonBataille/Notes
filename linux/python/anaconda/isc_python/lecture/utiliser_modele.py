import tensorflow as tf
from keras.models import load_model # Pour charger le modele
from keras.preprocessing import image # Pour importer l'image
import numpy as np

# Charger le modele
model=load_model('mon_modele.keras')

# Summary model
#model.summary()

# On transforme notre image en tenseur pour la passer au modele
def preprocess_image(mon_image):
	image_to_process = image.load_img(mon_image, target_size=(28, 28)) # Le modele a ete entraine par des images 28x28
	image_array = image.img_to_array(image_to_process)
	image_processed = np.empty([28, 28])
	for x in range(image_array.shape[0]):
		for y in range(image_array.shape[1]):
			rgb = image_array[x, y]
			rgb_flat = (rgb[0] + rgb[1] + rgb[2]) / 765.0
			image_processed[x][y] = rgb_flat
	# Ajoute un axe devant sans dimension pour signifier qu'il n'y a qu'une seule image
	# On cree un tenseur d'une seule ligne contenant l'image de 28x28
	# On ajoute une dimension au tenseur car on a entraine le modele avec un tenseur de 60000 images
	# Le tenseur de test est une matrice de 60000 lignes. Chaque ligne est une image de 28x28
	image_tensor = tf.expand_dims(image_processed, axis=0)
	return image_tensor

# On cree notre tenseur a partir de l'image
#tenseur = preprocess_image('num_8-8bit.jpg')
#tenseur = preprocess_image('output.png')
#print(tenseur)

# Prediction avec le modele que l'on a cree, on passe le tenseur
# predictions est un tenseur de 10 chiffres qui sont les probabilites que le tenseur appartienne a chaque classe [0,1,2,...,9]
#predictions = model.predict(tenseur)
#print(predictions)

# function
def quel_nombre(mon_image):
	tenseur = preprocess_image(mon_image)
	predictions = model.predict(tenseur)
	maxi = 0
	index_maxi = 0
	for idx in range(10):
		if predictions[0][idx] > maxi:
			maxi = predictions[0][idx]
			index_maxi = idx
		print(str(idx) + '=>' + str(round(predictions[0][idx] * 100, 3)) + '%')
	print('Le nombre sur l\'image ' + mon_image  + ' est ' + str(index_maxi))

quel_nombre('output.png')
