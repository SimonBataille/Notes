# Entraînement et Réglage des Poids et Biais dans GPT

Oui, pendant l’entraînement, l’objectif principal est de régler les **poids (\(w_{i,n}\))** et les **biais (\(b_n\))** des neurones dans la partie **linéaire** des couches du réseau de neurones. Ces poids et biais déterminent comment les données sont transformées à chaque étape. Voici une explication détaillée :

---

## 1. La partie linéaire : Transformation des tenseurs
Dans chaque couche d’un transformateur comme GPT, la partie linéaire est représentée par une transformation matricielle :
\[
z = W \cdot x + b
\]

### a. **Que signifient \(W\), \(x\), et \(b\) ?**
- **\(x\)** : Le vecteur d'entrée pour un neurone ou une couche (par exemple, une représentation contextuelle d’un token, de dimension \(d\)).
- **\(W\)** : Les poids appris par le modèle, une matrice de taille \((d_\text{output}, d_\text{input})\) qui détermine comment les dimensions de l'entrée sont combinées.
- **\(b\)** : Les biais appris par le modèle, des vecteurs ajoutés pour ajuster les valeurs en sortie.

### b. **Pourquoi régler \(W\) et \(b\) ?**
- \(W\) et \(b\) définissent comment chaque vecteur d’entrée est transformé en sortie.
- L’objectif de l’entraînement est de trouver les valeurs optimales pour \(W\) et \(b\) afin que le modèle génère les bonnes réponses.

---

## 2. Entraînement supervisé : Minimiser la perte
### a. **Objectif**
Pendant l’entraînement, on cherche à minimiser une fonction de perte (\(L\)), qui mesure l’écart entre la prédiction du modèle et la vérité terrain (réponse attendue).

### b. **Gradient de la perte par rapport aux poids**
Le modèle ajuste \(W\) et \(b\) en utilisant la **descente de gradient** :
\[
W \leftarrow W - \eta \frac{\partial L}{\partial W}, \quad b \leftarrow b - \eta \frac{\partial L}{\partial b}
\]
- **\(\frac{\partial L}{\partial W}\)** : Gradient de la perte par rapport aux poids. Cela indique dans quelle direction et avec quelle amplitude modifier \(W\) pour réduire \(L\).
- **\(\eta\)** : Le taux d’apprentissage, qui contrôle la vitesse d’ajustement.

---

## 3. Régler la partie non linéaire aussi
Bien que la partie linéaire (\(W \cdot x + b\)) soit centrale, la **non-linéarité** (via des fonctions comme ReLU ou GELU) joue également un rôle crucial :
- Les fonctions non linéaires ne contiennent pas de poids ajustables.
- Cependant, elles modifient comment les gradients se propagent dans le réseau, influençant indirectement l’entraînement.

---

## 4. Rôles des couches dans le réglage des poids
Dans GPT, plusieurs types de transformations linéaires nécessitent des poids ajustés :

### a. **Transformations dans l’attention multi-tête**
Pour chaque vecteur d'entrée (\(x\)), on calcule des projections linéaires :
1. **Query (\(Q\)) :**
   \[
   Q = W_Q \cdot x + b_Q
   \]
2. **Key (\(K\)) :**
   \[
   K = W_K \cdot x + b_K
   \]
3. **Value (\(V\)) :**
   \[
   V = W_V \cdot x + b_V
   \]
Ces projections sont réglées pour apprendre à quel point les tokens doivent s’influencer les uns les autres.

### b. **Couches feed-forward**
Après le mécanisme d’attention, les vecteurs passent dans un réseau feed-forward :
\[
z = W_1 \cdot x + b_1
\]
Puis :
\[
\text{sortie} = W_2 \cdot (\text{non-linéarité}(z)) + b_2
\]
Les poids (\(W_1, W_2\)) sont également réglés pendant l’entraînement.

---

## 5. Pourquoi autant de paramètres ?
### a. **Nombre de paramètres :**
GPT-4 est estimé à posséder **500 milliards de paramètres**, incluant :
- Les **matrices de poids** (\(W\)), qui composent la majorité des paramètres.
- Les **biais** (\(b\)), bien moins nombreux mais cruciaux pour le bon fonctionnement.

### b. **Exemple de dimensions dans une couche :**
Pour une seule couche avec une dimension interne de \(12288\) :
- Matrices pour Query (\(W_Q\)), Key (\(W_K\)), et Value (\(W_V\)) : chacune de taille \(12288 \times 12288\).
- Poids pour les feed-forward : par exemple, \(12288 \times 4 \cdot 12288\) (augmentation temporaire pour enrichir les relations).

Avec 96 couches et plusieurs têtes d’attention, le nombre total de paramètres monte rapidement dans les **centaines de milliards**.

---

## 6. En résumé
- **Poids (\(W\))** : Matrices déterminant comment les vecteurs d’entrée sont transformés.
- **Biais (\(b\))** : Vecteurs ajustant les valeurs de sortie.
- Pendant l’entraînement, ces paramètres sont ajustés pour minimiser une fonction de perte, permettant au modèle d’apprendre les relations contextuelles nécessaires pour répondre aux requêtes avec précision.
