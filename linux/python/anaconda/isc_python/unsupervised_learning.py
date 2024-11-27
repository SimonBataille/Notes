from sklearn import datasets
from sklearn.cluster import KMeans #import du modele d'IA kMeans
import matplotlib.pyplot as plt
import numpy as np


iris = datasets.load_iris()
x = iris.data
#print(x)


# On cree puis on entraine notre modele avec les donnees d'iris
kmeans=KMeans(n_clusters=3) # on sait qu'il y a 3 especes d'Iris differentes
kmeans.fit(x)
#print(kmeans.labels_) # numpy.ndarray' : [0 0 0 0 ...]
#print(type(kmeans.labels_)) # on peut passer kmeans.labels_ a plt.scatter


# On utilise les 3 centres du modele
centers = kmeans.cluster_centers_
#plt.scatter(centers[:,2], centers[:,3], c='red', marker='X', s=200)
#print(centers)


# On simule les preferences des clients
client_preferences = np.array([
    [5.1, 3.5, 1.4, 0.2], #client 0 : caracteristiques de fleur preferee
    [6.2, 2.8, 4.1, 1.8], #client 1
    [7.9, 4.1, 6.2, 2.3] #client 2
])
#plt.scatter(client_preferences[:,2], client_preferences[:,3], c='green', marker='o', s=200)


# On demade au model quel type d'iris est adapte
# Exemple permet de regrouper les clients par habitude de consommation
clients_segments = kmeans.predict(client_preferences)
print(clients_segments.tolist()) # [0, 1, 2] : iris du groupe/cluster 0 pour client 0 ...


# Plot en nuage de point
plt.scatter(x[:,2], x[:,3], c=kmeans.labels_)
plt.title('Dataset Iiris')
plt.xlabel('Longueur petale')
plt.ylabel('Largeur petale')
plt.show()
