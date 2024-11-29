# 1. Résumé du fonctionnement

Entrée texte → Tokens → Tenseurs [12288]/token → Modèle (décodeur, non-linéarité, attention...) → Représentation contextuelle → Calcul de probabilité → Sélection du prochain token → Boucle répétée

# 2. Tout est-il fait dans le décodeur ?

Oui, dans des modèles comme GPT, tout le traitement est effectué par le décodeur, car :

- Il n’y a pas d’encodeur distinct comme dans les modèles encodeur-décodeur (par exemple, pour la traduction).
- Le décodeur traite directement l’entrée et génère la sortie de manière auto-régressive (token par token).

Dans GPT :

- Le texte d’entrée est transformé en tokens.
- Ces tokens sont immédiatement traités par le décodeur.
- La génération du texte suit un processus itératif, chaque étape s’appuyant sur les représentations contextuelles calculées pour l'entrée et les tokens précédemment générés.

# 3. Représentation contextuelle calculée pour toute l’entrée

Avant de générer quoi que ce soit, le décodeur calcule d’abord une représentation contextuelle complète pour tous les tokens de l’entrée, grâce au mécanisme d'auto-attention (*self-attention*).

**Processus :**

1. **Auto-attention sur l’entrée complète :**
   - Le modèle analyse toutes les relations possibles entre les tokens de l’entrée.
   - Par exemple, dans la phrase "Le chat mange une souris", le décodeur comprend que "mange" est lié à "chat" (sujet) et "souris" (objet).

2. **Représentation contextuelle obtenue :**
   - Chaque token est associé à un vecteur de représentation contextuelle.
   - Ces vecteurs capturent les relations entre les tokens dans le contexte de la séquence d’entrée.

3. **Dimension de la représentation contextuelle :**
   - Pour chaque token, la représentation contextuelle est un vecteur de 12288 dimensions dans GPT-3/4.
   - Ainsi, pour une séquence d’entrée avec N tokens, le décodeur produit un tenseur de taille :  
     *(Batch size) × N × 12288*

# 4. La génération est-elle basée uniquement sur l'entrée ou aussi sur la sortie générée ?

### a. Calcul initial pour l’entrée complète

- Le modèle commence par analyser toute l’entrée texte et produit des représentations contextuelles pour ces tokens.

### b. Itération avec les tokens générés

- Une fois le premier token généré, le modèle réévalue le contexte à chaque étape.
- Les tokens générés sont ajoutés à l’entrée et inclus dans les calculs pour ajuster les représentations contextuelles.

# 5. Calcul des probabilités

Une fois les représentations contextuelles obtenues, voici comment le modèle génère le prochain token :

1. **Projection linéaire :**
   - Les représentations contextuelles (12288 dimensions) sont projetées dans l’espace du vocabulaire (50000 dimensions dans GPT-3/4).
   - Cela donne un vecteur de probabilités pour chaque mot possible.

2. **Probabilité normalisée :**
   - Une fonction softmax transforme ces scores en probabilités :  
     \( P(token_i) = \frac{e^{s_i}}{\sum_j e^{s_j}} \)  
     Où \( s_i \) est le score non normalisé pour le token \( i \).

3. **Sélection du token :**
   - Le token avec la plus grande probabilité est choisi (ou via une méthode comme *sampling* ou *top-k*).

# 6. La représentation contextuelle est-elle un vecteur [12288] ?

Oui :

- Chaque token est représenté par un vecteur de 12288 dimensions après avoir traversé le décodeur.
- Ce vecteur est enrichi par le mécanisme d'attention multi-tête et les couches feed-forward pour inclure le contexte global.

**Exemple pour une phrase :**

- Si votre entrée contient 10 tokens, vous obtiendrez une matrice de taille :  
  \( 10 × 12288 \)  
  Chaque ligne correspond à la représentation contextuelle d’un token.

# 7. Pourquoi recalculer les contextes à chaque étape ?

La génération étant auto-régressive, chaque nouveau token modifie le contexte :

- Lorsqu’un nouveau token est ajouté, les relations contextuelles doivent être réévaluées.
- Le mécanisme d’auto-attention est recalculé pour tenir compte de la séquence complète (entrée + tokens générés).

# 8. Résumé simplifié

- **Entrée complète analysée :**
  - Le décodeur transforme tous les tokens d’entrée en une représentation contextuelle riche (vecteurs de 12288 dimensions).

- **Génération itérative :**
  - À chaque étape, le modèle utilise ces représentations pour prédire le prochain token.
  - Les représentations sont mises à jour en intégrant les tokens générés.

Ce processus garantit que chaque token est généré en tenant compte du contexte global (entrée et sortie déjà générée).


# 9. Schema Python 
```
import matplotlib.pyplot as plt

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Add text boxes for each step
ax.text(0.1, 0.9, "1. Entrée texte\n→ Tokenisation\n→ Tenseurs (12288/token)", 
        bbox=dict(boxstyle="round", facecolor="lightblue", edgecolor="black"), fontsize=10, ha='left')

ax.text(0.1, 0.7, "2. Passage dans le décodeur\n→ Mécanisme d'attention multi-tête\n→ Couches feed-forward\n→ Représentation contextuelle",
        bbox=dict(boxstyle="round", facecolor="lightgreen", edgecolor="black"), fontsize=10, ha='left')

ax.text(0.1, 0.5, "3. Représentation contextuelle\n→ Vecteurs (12288/token) générés pour chaque token d'entrée", 
        bbox=dict(boxstyle="round", facecolor="lightyellow", edgecolor="black"), fontsize=10, ha='left')

ax.text(0.1, 0.3, "4. Génération du prochain token\n→ Calcul des probabilités (via softmax)\n→ Sélection du token suivant",
        bbox=dict(boxstyle="round", facecolor="lightpink", edgecolor="black"), fontsize=10, ha='left')

ax.text(0.1, 0.1, "5. Boucle auto-régressive\n→ Ajout du token généré au contexte\n→ Recalcul des représentations contextuelles",
        bbox=dict(boxstyle="round", facecolor="lightcoral", edgecolor="black"), fontsize=10, ha='left')

# Draw arrows between the steps
ax.annotate("", xy=(0.5, 0.85), xytext=(0.5, 0.72),
            arrowprops=dict(facecolor="black", arrowstyle="->"))
ax.annotate("", xy=(0.5, 0.67), xytext=(0.5, 0.52),
            arrowprops=dict(facecolor="black", arrowstyle="->"))
ax.annotate("", xy=(0.5, 0.47), xytext=(0.5, 0.32),
            arrowprops=dict(facecolor="black", arrowstyle="->"))
ax.annotate("", xy=(0.5, 0.27), xytext=(0.5, 0.12),
            arrowprops=dict(facecolor="black", arrowstyle="->"))

# Hide axes for clarity
ax.axis('off')

# Display the flowchart
plt.title("Résumé schématique du fonctionnement de la génération de texte", fontsize=12, weight='bold')
plt.tight_layout()
plt.show()
```
