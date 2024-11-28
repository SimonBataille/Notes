# Resume

Entrée texte → Tokens → Tenseurs [12288]/token → Modèle (décodeur, non-linéarité, attention...) → Représentation contextuelle → Calcul de probabilité → Sélection du prochain token → Boucle répétée

## 
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
