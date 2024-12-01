# Si vous utilisez Conda, installez la bibliothèque 'llama-cpp-python' via la commande suivante
# conda install conda-forge::llama-cpp-python

from llama_cpp import Llama  # Importation de la classe Llama depuis la bibliothèque llama-cpp

# Chargement du modèle Llama avec les paramètres spécifiés
# Le modèle est situé à './llama-2-7b.Q3_K_S.gguf'. 
# Nous spécifions également 'verbose=False' pour éviter les logs détaillés et 'n_ctx=2048' pour définir la taille du contexte
#llm = Llama(model_path='./llama-2-7b.Q3_K_S.gguf', verbose=False)
llm = Llama(model_path='./llama-2-7b.Q3_K_S.gguf', verbose=False, n_ctx=2048)

# Demande à l'utilisateur une entrée via le prompt
prompt = input('Que puis-je pour vous ? ')  # Affiche un message pour interroger l'utilisateur

print('Un instant...')  # Indique à l'utilisateur que le traitement est en cours

# Utilisation de l'instance 'llm' pour générer une réponse à partir du prompt.
# On spécifie 'max_tokens=500' pour limiter la réponse à 500 tokens maximum
# La ligne ci-dessous est commentée car elle ne contient pas la limite de tokens
# sortie = llm(prompt)
sortie = llm(prompt, max_tokens=500)  # Génère la sortie du modèle Llama

# Affichage complet de la sortie générée (pour une inspection brute de ce qui est retourné)
print(sortie)

# Affichage du texte généré, qui se trouve dans la première option des choix retournés par le modèle
print(sortie['choices'][0]['text'])  # Accède et affiche uniquement le texte de la première réponse

'''
Corrections et commentaires :

    Installation Conda : J'ai ajouté un commentaire plus clair sur la ligne # si conda pour spécifier que la commande est à utiliser dans un environnement Conda.
    Paramètres de modèle : J'ai précisé les paramètres de votre modèle Llama et expliqué l'option n_ctx=2048, qui ajuste la taille du contexte pour la génération.
    Commentaire sur l'appel à llm(prompt) : J'ai détaillé l'utilisation de max_tokens=500, qui limite la réponse à 500 tokens.
    Clarification de la sortie : J'ai ajouté des commentaires pour expliquer la différence entre l'affichage complet de la sortie (print(sortie)) et l'accès au texte généré dans sortie['choices'][0]['text'].
'''
