# Importation des bibliothèques nécessaires depuis la bibliothèque Hugging Face
from transformers import pipeline

# Création d'un pipeline pour la génération de texte
# 'text-generation' : spécifie que le pipeline doit être utilisé pour générer du texte.
# 'model="gpt2"' : utilise le modèle GPT-2 pré-entraîné.
generator = pipeline("text-generation", model="gpt2")

# Utilisation du pipeline pour générer du texte
# La phrase "Le futur de l'IA est" est utilisée comme prompt de départ.
# 'max_length=30' : limite la longueur totale du texte généré à 30 tokens.
# 'num_return_sequences=1' : demande une seule séquence de texte générée.
result = generator("Le futur de l'IA est", max_length=30, num_return_sequences=1)

# Affichage du résultat généré par le modèle
# Le résultat est une liste de dictionnaires contenant le texte généré.
print(result)


'''
Explication globale :

    1. Pipeline : Crée un pipeline pour gérer facilement les tâches NLP (ici, génération de texte).
    2. Modèle pré-entraîné : Utilise GPT-2, un modèle génératif bien connu.
    3. Génération de texte : Prend un prompt ("Le futur de l'IA est") et génère une continuation jusqu'à 30 tokens.
    4. Affichage des résultats : Montre la sortie générée sous forme de liste, où chaque élément contient un texte généré.
'''
