from keras.datasets import mnist # jeu de donnees
from keras.models import Sequential # c'est un model sequentiel
from keras.layers import Dense, Flatten # Dense : couche interne, Flatten : applatir l'image comme une suite de nombre

# Charge les donnees
# 1 label par image, 10 labels : 0, 1, 2, ...
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalise les images car le modele necessite des valeurs entre [0, 1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# Model sequentiel a 3 couches : entree (applatir l'image), interne/cachee (reseau de neurones), sortie (10 neurones : probalitite que l'image appartiennent a un des 10 labels)
model = Sequential([
	Flatten(input_shape=(28,28)),
	Dense(units=128, activation='relu'), # relu : on appuit plus fort sur le crayon
	Dense(10, activation='softmax') # softmax : somme des % = 1
])

# Compile le modele
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Sommaire du modele
# en entree vecteur[28x28] = vecteur[784]
# au milieu reseau de 128 neuronnes soit 128x(784+1)=128x785=100480 parametres
# en sortie un resultat en forme de reseau de 10 neuronnes de (128+1)x10=1290 parametres
#model.summary()

# Entrainement du modele
model.fit(train_images, train_labels, epochs=15)

# Evaluer le modele entraine grace aux donnes de test
model.evaluate(test_images, test_labels)

# Sauvegarde du modele au format keras natif pour ne pas le re-entrainer a chaque fois
# On va utiliser ce modele dans un autre script et voir s'il est capable de lire les images qu'on lui passe
# Il faut mettre les images sous formes de tenseurs (matrices de nombres) car le modele ne comprends pas les formats images type jpg...
model.save('mon_modele.keras')
